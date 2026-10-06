"""Evalúa una batería de modelos con validación repetida y guarda los resultados por partición.

Genera los archivos que piden las etapas 3 y 4 de la ruta:

- results/tables/metricas_por_particion.csv  (una fila por modelo, partición y métrica)
- results/tables/resumen_modelos.csv         (media ± desviación estándar y tiempo de ajuste)
- results/experiments.csv                     (una fila por corrida: fecha, modelo, parámetros, semilla y métricas)

Uso típico (en Colab o en un script):

    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.dummy import DummyClassifier
    from bateria_modelos import esquema_validacion, evaluar_bateria

    modelos = {
        "Línea base": DummyClassifier(strategy="most_frequent"),
        "Regresión logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    }
    cv = esquema_validacion("clasificacion", n_splits=5, n_repeats=2)
    resumen, por_particion = evaluar_bateria(modelos, X_train, y_train, cv,
                                             metricas=["f1_macro", "roc_auc"])

Todo el preprocesamiento debe ir dentro de cada Pipeline para que se ajuste solo con los datos
de entrenamiento de cada partición (así se evita la fuga de información).
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import (RepeatedKFold, RepeatedStratifiedKFold,
                                     TimeSeriesSplit, cross_validate)

SEMILLA = 42


def esquema_validacion(tipo="clasificacion", n_splits=5, n_repeats=2, temporal=False, semilla=SEMILLA):
    """Devuelve el esquema de validación del protocolo.

    tipo: "clasificacion" (estratificada) o "regresion".
    temporal=True usa TimeSeriesSplit (sin barajar, respeta el orden del tiempo).
    """
    if temporal:
        return TimeSeriesSplit(n_splits=n_splits)
    if tipo == "clasificacion":
        return RepeatedStratifiedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=semilla)
    return RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats, random_state=semilla)


def _pliegues_por_repeticion(cv):
    if hasattr(cv, "cvargs"):          # RepeatedKFold y RepeatedStratifiedKFold
        return cv.cvargs["n_splits"]
    return cv.get_n_splits()           # TimeSeriesSplit, KFold, etc.


def _nombre_metrica(nombre):
    """'neg_root_mean_squared_error' -> 'root_mean_squared_error' (y el valor se cambia de signo)."""
    return (nombre[4:], -1.0) if nombre.startswith("neg_") else (nombre, 1.0)


def _parametros(modelo):
    """Parámetros del último paso del modelo, en texto, para el registro de experimentos."""
    final = modelo.steps[-1][1] if hasattr(modelo, "steps") else modelo
    params = {k: v for k, v in final.get_params(deep=False).items()
              if isinstance(v, (int, float, str, bool, type(None)))}
    return json.dumps({"modelo": type(final).__name__, **params}, ensure_ascii=False, default=str)


def evaluar_bateria(modelos, X, y, cv, metricas, carpeta="results", semilla=SEMILLA,
                    registrar=True, n_jobs=None):
    """Evalúa cada modelo con el mismo esquema `cv` y guarda los resultados.

    modelos: diccionario {"nombre": estimador o Pipeline}.
    metricas: lista o diccionario de *scorers* de scikit-learn, p. ej. ["f1_macro", "roc_auc"] o
              ["neg_root_mean_squared_error", "neg_mean_absolute_error", "r2"].
    Devuelve (resumen, por_particion) como DataFrames.
    """
    carpeta = Path(carpeta)
    (carpeta / "tables").mkdir(parents=True, exist_ok=True)
    k = _pliegues_por_repeticion(cv)
    nombres = list(metricas) if isinstance(metricas, (list, tuple)) else list(metricas.keys())

    filas, resumen = [], []
    for nombre_modelo, modelo in modelos.items():
        res = cross_validate(modelo, X, y, cv=cv, scoring=metricas, n_jobs=n_jobs,
                             return_train_score=False, error_score="raise")
        n_part = len(res["fit_time"])
        fila_resumen = {"modelo": nombre_modelo,
                        "tiempo_ajuste_s": float(np.mean(res["fit_time"])),
                        "particiones": n_part}
        for m in nombres:
            limpio, signo = _nombre_metrica(m)
            valores = signo * res[f"test_{m}"]
            for i, v in enumerate(valores):
                filas.append({"modelo": nombre_modelo, "repeticion": i // k + 1, "pliegue": i % k + 1,
                              "metrica": limpio, "valor": float(v)})
            fila_resumen[f"{limpio}_media"] = float(np.mean(valores))
            fila_resumen[f"{limpio}_de"] = float(np.std(valores, ddof=1)) if n_part > 1 else 0.0
        resumen.append(fila_resumen)

        if registrar:
            exp = carpeta / "experiments.csv"
            registro = pd.DataFrame([{
                "fecha": dt.datetime.now().isoformat(timespec="seconds"),
                "modelo": nombre_modelo,
                "parametros": _parametros(modelo),
                "semilla": semilla,
                "validacion": type(cv).__name__,
                "metricas": json.dumps({c: round(v, 6) for c, v in fila_resumen.items()
                                        if c.endswith(("_media", "_de"))}, ensure_ascii=False),
            }])
            registro.to_csv(exp, mode="a", header=not exp.exists(), index=False)

    por_particion = pd.DataFrame(filas)
    resumen = pd.DataFrame(resumen)
    por_particion.to_csv(carpeta / "tables" / "metricas_por_particion.csv", index=False)
    resumen.to_csv(carpeta / "tables" / "resumen_modelos.csv", index=False)
    return resumen, por_particion


def tabla_media_de(resumen, metrica, decimales=3, mayor_es_mejor=True):
    """Tabla lista para el documento: «Modelo | métrica (media ± DE) | tiempo», ordenada."""
    t = resumen[["modelo", f"{metrica}_media", f"{metrica}_de", "tiempo_ajuste_s"]].copy()
    t = t.sort_values(f"{metrica}_media", ascending=not mayor_es_mejor)
    t[metrica] = (t[f"{metrica}_media"].round(decimales).astype(str) + " ± "
                  + t[f"{metrica}_de"].round(decimales).astype(str))
    t["tiempo_ajuste_s"] = t["tiempo_ajuste_s"].round(3)
    return t[["modelo", metrica, "tiempo_ajuste_s"]].reset_index(drop=True)


if __name__ == "__main__":
    # Demostración con un conjunto de datos incluido en scikit-learn.
    from sklearn.datasets import load_breast_cancer
    from sklearn.dummy import DummyClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    modelos = {
        "Línea base": DummyClassifier(strategy="most_frequent"),
        "Regresión logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=SEMILLA),
    }
    cv = esquema_validacion("clasificacion", n_splits=5, n_repeats=2)
    resumen, por_particion = evaluar_bateria(modelos, X, y, cv, ["f1_macro", "roc_auc"],
                                             carpeta="results_demo", registrar=False)
    print(tabla_media_de(resumen, "f1_macro"))
    assert len(por_particion) == 3 * 10 * 2, "faltan filas en metricas_por_particion"

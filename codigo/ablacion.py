"""Tabla de ablación: qué aporta cada decisión de tu modelo final.

Parte del modelo completo y quita una decisión a la vez (las variables que creaste, el balanceo de
clases, la selección de variables, la optimización de hiperparámetros…), con el MISMO esquema de
validación del protocolo. Para cada variante reporta la métrica principal con su intervalo de
confianza y la diferencia frente al modelo completo, y guarda results/tables/ablacion.csv.

Uso típico:

    from ablacion import ablacion
    variantes = {
        "Modelo completo": (modelo_final, todas_las_columnas),
        "Sin variables creadas": (modelo_final, columnas_originales),
        "Sin balanceo de clases": (modelo_sin_smote, todas_las_columnas),
        "Hiperparámetros por defecto": (modelo_por_defecto, todas_las_columnas),
    }
    tabla = ablacion(variantes, X_train, y_train, cv, "f1_macro")

Cada variante puede ser solo un estimador (usa todas las columnas) o una tupla (estimador, columnas).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.model_selection import cross_val_score

from intervalos_confianza import ic_particiones


def _tamanos(cv, X, y):
    tr, te = next(iter(cv.split(X, y)))
    return len(tr), len(te)


def ablacion(variantes, X, y, cv, metrica, referencia=None, carpeta="results", n_jobs=None):
    """Evalúa cada variante con el mismo `cv` y compara contra la `referencia` (la primera, por defecto).

    metrica: un *scorer* de scikit-learn ("f1_macro", "roc_auc", "neg_root_mean_squared_error", …).
    Las métricas "neg_…" se reportan en positivo (p. ej. RMSE), donde menor es mejor.
    """
    signo = -1.0 if metrica.startswith("neg_") else 1.0
    nombre_metrica = metrica[4:] if metrica.startswith("neg_") else metrica
    n_train, n_test = _tamanos(cv, X, y)
    referencia = referencia or next(iter(variantes))

    puntajes = {}
    for nombre, var in variantes.items():
        est, cols = var if isinstance(var, tuple) else (var, None)
        Xv = X[cols] if cols is not None else X
        puntajes[nombre] = signo * cross_val_score(clone(est), Xv, y, cv=cv, scoring=metrica, n_jobs=n_jobs)

    filas = []
    for nombre, v in puntajes.items():
        ic = ic_particiones(v, n_train, n_test)
        dif = v - puntajes[referencia]
        ic_dif = ic_particiones(dif, n_train, n_test) if nombre != referencia else None
        filas.append({
            "variante": nombre,
            f"{nombre_metrica}_media": ic["media"],
            "ic95_inferior": ic["ic_inferior"],
            "ic95_superior": ic["ic_superior"],
            "diferencia_vs_referencia": float(dif.mean()) if ic_dif else 0.0,
            "dif_ic95_inferior": ic_dif["ic_inferior"] if ic_dif else np.nan,
            "dif_ic95_superior": ic_dif["ic_superior"] if ic_dif else np.nan,
            "diferencia_incluye_cero": (ic_dif["ic_inferior"] <= 0 <= ic_dif["ic_superior"]) if ic_dif else np.nan,
        })
    tabla = pd.DataFrame(filas)
    Path(carpeta, "tables").mkdir(parents=True, exist_ok=True)
    tabla.to_csv(Path(carpeta, "tables", "ablacion.csv"), index=False)
    return tabla


if __name__ == "__main__":
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import RepeatedStratifiedKFold

    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    rf = RandomForestClassifier(n_estimators=200, random_state=42)
    cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=2, random_state=42)
    variantes = {
        "Modelo completo (30 variables)": rf,
        "Sin variables «worst»": (rf, [c for c in X.columns if not c.startswith("worst")]),
        "Solo variables «mean»": (rf, [c for c in X.columns if c.startswith("mean")]),
        "Árboles poco profundos": RandomForestClassifier(n_estimators=200, max_depth=2, random_state=42),
    }
    print(ablacion(variantes, X, y, cv, "f1_macro", carpeta="results_demo").round(4).to_string())

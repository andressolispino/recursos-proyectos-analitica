"""Explicabilidad del mejor modelo con SHAP, contrastada con la importancia por permutación.

Genera las figuras que pide la etapa 4 de la ruta (en results/figures/, PNG a 300 dpi):

- shap_resumen.png         gráfico de enjambre (beeswarm) con todas las variables importantes
- shap_importancia.png     importancia global (media del |SHAP|)
- shap_dependencia_<var>.png  dependencia de las 3 variables principales
- shap_caso_<i>.png        explicación de casos individuales (waterfall)

y las tablas results/tables/importancia_shap.csv e importancia_permutacion.csv.

Uso típico:

    from explicabilidad import explicar_shap, importancia_permutacion, comparar_importancias
    imp_shap = explicar_shap(mejor_modelo, X_train, X_test, casos=[0, 5, 10])
    imp_perm = importancia_permutacion(mejor_modelo, X_test, y_test, metrica="f1_macro")
    comparar_importancias(imp_shap, imp_perm)

Recuerda: SHAP explica lo que hace el MODELO, no causas del fenómeno. Interprétalo en el lenguaje del
problema y contrástalo con otro método (importancia por permutación) antes de concluir.
"""
from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.inspection import permutation_importance

SEMILLA = 42


def _separar_pipeline(modelo):
    """Devuelve (preprocesamiento o None, estimador final)."""
    if hasattr(modelo, "steps") and len(modelo.steps) > 1:
        return modelo[:-1], modelo[-1]
    if hasattr(modelo, "steps"):
        return None, modelo[-1]
    return None, modelo


def _transformar(prep, X):
    if prep is None:
        return X
    Xt = prep.transform(X)
    try:
        nombres = prep.get_feature_names_out()
    except Exception:
        nombres = [f"x{i}" for i in range(Xt.shape[1])]
    Xt = Xt.toarray() if hasattr(Xt, "toarray") else Xt
    return pd.DataFrame(Xt, columns=nombres, index=getattr(X, "index", None))


def _guardar(ruta):
    plt.gcf().savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close("all")


def explicar_shap(modelo, X_fondo, X_explicar, casos=(0, 1, 2), clase=None, top=3,
                  max_fondo=100, max_explicar=1000, carpeta="results"):
    """Calcula los valores SHAP del modelo ya entrenado y guarda figuras y tabla de importancia.

    X_fondo: datos de referencia (normalmente una muestra de entrenamiento).
    X_explicar: datos a explicar (normalmente prueba).
    clase: en clasificación, la clase cuyo SHAP se grafica (por defecto la positiva o la última).
    """
    import shap

    figs = Path(carpeta, "figures")
    tabs = Path(carpeta, "tables")
    figs.mkdir(parents=True, exist_ok=True)
    tabs.mkdir(parents=True, exist_ok=True)

    prep, final = _separar_pipeline(modelo)
    Xb = _transformar(prep, X_fondo)
    Xe = _transformar(prep, X_explicar)
    Xb = Xb.sample(min(max_fondo, len(Xb)), random_state=SEMILLA) if hasattr(Xb, "sample") else Xb[:max_fondo]
    Xe = Xe.iloc[:max_explicar] if hasattr(Xe, "iloc") else Xe[:max_explicar]

    try:
        sv = shap.Explainer(final, Xb)(Xe)
    except Exception:
        # Modelos sin explicador específico: método por permutación sobre la función de predicción.
        f = final.predict_proba if hasattr(final, "predict_proba") else final.predict
        sv = shap.Explainer(f, Xb, seed=SEMILLA)(Xe)

    if sv.values.ndim == 3:   # clasificación: (filas, variables, clases)
        idx = clase if clase is not None else sv.values.shape[2] - 1
        sv = sv[:, :, idx]

    importancia = (pd.DataFrame({"variable": sv.feature_names, "shap_abs_medio": np.abs(sv.values).mean(axis=0)})
                   .sort_values("shap_abs_medio", ascending=False).reset_index(drop=True))
    importancia.to_csv(tabs / "importancia_shap.csv", index=False)

    shap.plots.beeswarm(sv, max_display=15, show=False)
    _guardar(figs / "shap_resumen.png")
    shap.plots.bar(sv, max_display=15, show=False)
    _guardar(figs / "shap_importancia.png")
    for var in importancia["variable"].head(top):
        shap.plots.scatter(sv[:, var], color=sv, show=False)
        _guardar(figs / f"shap_dependencia_{re.sub(r'[^A-Za-z0-9_]+', '_', str(var))}.png")
    for i in casos:
        if i < len(sv.values):
            shap.plots.waterfall(sv[i], max_display=12, show=False)
            _guardar(figs / f"shap_caso_{i}.png")
    return importancia


def importancia_permutacion(modelo, X, y, metrica, n_repeats=20, carpeta="results", n_jobs=None):
    """Importancia por permutación sobre datos que el modelo no usó para entrenar (prueba)."""
    r = permutation_importance(modelo, X, y, scoring=metrica, n_repeats=n_repeats,
                               random_state=SEMILLA, n_jobs=n_jobs)
    tabla = (pd.DataFrame({"variable": list(X.columns), "importancia_media": r.importances_mean,
                           "importancia_de": r.importances_std})
             .sort_values("importancia_media", ascending=False).reset_index(drop=True))
    Path(carpeta, "tables").mkdir(parents=True, exist_ok=True)
    tabla.to_csv(Path(carpeta, "tables", "importancia_permutacion.csv"), index=False)
    return tabla


def comparar_importancias(imp_shap, imp_perm, top=10):
    """Correlación de Spearman entre los dos rankings y coincidencias en el top.

    Si el modelo transforma variables (p. ej. one-hot), compara solo las que conservan el nombre.
    """
    s = imp_shap.assign(variable=imp_shap["variable"].astype(str).str.replace(r"^\w+__", "", regex=True))
    m = s.merge(imp_perm, on="variable", how="inner")
    if len(m) < 3:
        raise ValueError("Muy pocas variables en común para comparar: revisa los nombres.")
    rho, p = stats.spearmanr(m["shap_abs_medio"], m["importancia_media"])
    comunes = set(s["variable"].head(top)) & set(imp_perm["variable"].head(top))
    return {"spearman_rho": float(rho), "p_valor": float(p), "variables_comparadas": len(m),
            f"coinciden_en_top_{top}": sorted(comunes)}


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    from sklearn.datasets import load_breast_cancer
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=SEMILLA)
    rf = RandomForestClassifier(n_estimators=200, random_state=SEMILLA).fit(X_tr, y_tr)
    imp_s = explicar_shap(rf, X_tr, X_te, casos=[0, 1], carpeta="results_demo")
    imp_p = importancia_permutacion(rf, X_te, y_te, "f1_macro", n_repeats=5, carpeta="results_demo")
    print(imp_s.head())
    print(comparar_importancias(imp_s, imp_p))

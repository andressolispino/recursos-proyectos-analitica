"""Comparación estadística de modelos a partir de results/tables/metricas_por_particion.csv.

Incluye lo que pide la etapa 4 de la ruta:

- Prueba de Friedman sobre los rangos de los modelos en cada partición.
- Post hoc de Nemenyi con su diferencia crítica (CD) y el diagrama de diferencia crítica.
- Alternativa por pares: Wilcoxon de rangos con signo con corrección de Holm.

Uso típico:

    from comparacion_estadistica import (matriz_desempeno, friedman, nemenyi,
                                         diagrama_diferencia_critica, wilcoxon_holm)
    M = matriz_desempeno("results/tables/metricas_por_particion.csv", "f1_macro")
    fr = friedman(M, mayor_es_mejor=True)
    cd = nemenyi(fr["rangos_promedio"], n_bloques=len(M))
    diagrama_diferencia_critica(fr["rangos_promedio"], cd, "results/figures/diferencia_critica.png")
    pares = wilcoxon_holm(M, mayor_es_mejor=True)

Advertencia metodológica: las particiones de una validación cruzada repetida comparten datos, así
que no son del todo independientes. Estas pruebas son un apoyo para ordenar la evidencia, no una
garantía; repórtalas junto con los intervalos de confianza y discute esta limitación.
Referencia: Demšar, J. (2006). Statistical comparisons of classifiers over multiple data sets.
Journal of Machine Learning Research, 7, 1–30.
"""
from __future__ import annotations

from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


def matriz_desempeno(ruta_o_df, metrica):
    """Devuelve una matriz con una fila por partición (repetición, pliegue) y una columna por modelo."""
    df = pd.read_csv(ruta_o_df) if isinstance(ruta_o_df, (str, Path)) else ruta_o_df
    df = df[df["metrica"] == metrica]
    if df.empty:
        raise ValueError(f"No hay filas para la métrica '{metrica}'.")
    M = df.pivot_table(index=["repeticion", "pliegue"], columns="modelo", values="valor")
    if M.isna().any().any():
        raise ValueError("Hay particiones sin resultado para algún modelo: revisa el CSV.")
    return M


def friedman(M, mayor_es_mejor=True):
    """Prueba de Friedman. Rango 1 = mejor modelo en cada partición."""
    if M.shape[1] < 3:
        raise ValueError("Friedman necesita al menos 3 modelos; con 2 usa wilcoxon_holm.")
    estadistico, p = stats.friedmanchisquare(*[M[c].values for c in M.columns])
    rangos = M.rank(axis=1, ascending=not mayor_es_mejor)
    return {"estadistico": float(estadistico), "p_valor": float(p),
            "n_bloques": len(M), "k_modelos": M.shape[1],
            "rangos_promedio": rangos.mean().sort_values()}


def nemenyi(rangos_promedio, n_bloques, alpha=0.05):
    """Diferencia crítica de Nemenyi: dos modelos difieren si sus rangos promedio difieren más que CD."""
    k = len(rangos_promedio)
    q_alpha = stats.studentized_range.ppf(1 - alpha, k, np.inf) / np.sqrt(2)
    return float(q_alpha * np.sqrt(k * (k + 1) / (6.0 * n_bloques)))


def _grupos_sin_diferencia(rangos, cd):
    """Grupos maximales de modelos consecutivos cuya diferencia de rango es menor que CD."""
    r = rangos.values
    grupos = []
    for i in range(len(r)):
        j = i
        while j + 1 < len(r) and r[j + 1] - r[i] < cd:
            j += 1
        if j > i and not any(a <= i and j <= b for a, b in grupos):
            grupos.append((i, j))
    return grupos


def diagrama_diferencia_critica(rangos_promedio, cd, ruta=None, titulo=None):
    """Dibuja el diagrama de diferencia crítica (Demšar, 2006). Devuelve la figura de matplotlib."""
    import matplotlib.pyplot as plt

    rangos = rangos_promedio.sort_values()
    k = len(rangos)
    nombres = list(rangos.index)
    mitad = (k + 1) // 2
    filas_etiquetas = max(mitad, k - mitad)
    fondo = -0.45 - 0.35 * (filas_etiquetas - 1)
    fig, ax = plt.subplots(figsize=(9, 1.4 + 0.35 * filas_etiquetas))
    ax.set_xlim(0.5, k + 0.5)
    ax.set_ylim(fondo - 0.25, 1.4)
    ax.axis("off")

    # Eje de rangos (1 = mejor, a la izquierda).
    ax.hlines(0, 1, k, color="black", lw=1)
    for t in range(1, k + 1):
        ax.vlines(t, 0, 0.12, color="black", lw=1)
        ax.text(t, 0.2, str(t), ha="center", va="bottom", fontsize=9)

    # Barra de la diferencia crítica.
    ax.hlines(1.0, 1, 1 + cd, color="black", lw=2)
    ax.vlines([1, 1 + cd], 0.93, 1.07, color="black", lw=2)
    ax.text(1 + cd / 2, 1.12, f"CD = {cd:.2f}", ha="center", va="bottom", fontsize=9)

    # Etiquetas de los modelos: la mitad a la izquierda y la mitad a la derecha.
    for i, (nombre, r) in enumerate(rangos.items()):
        izquierda = i < mitad
        fila = i if izquierda else (k - 1 - i)
        y = -0.45 - 0.35 * fila
        x_texto = 0.6 if izquierda else k + 0.4
        ax.vlines(r, y, 0, color="gray", lw=0.8)
        ax.hlines(y, min(r, x_texto), max(r, x_texto), color="gray", lw=0.8)
        ax.text(x_texto - 0.05 if izquierda else x_texto + 0.05, y, f"{nombre} ({r:.2f})",
                ha="right" if izquierda else "left", va="center", fontsize=9)

    # Barras gruesas: grupos sin diferencia significativa.
    for n, (a, b) in enumerate(_grupos_sin_diferencia(rangos, cd)):
        y = -0.18 - 0.08 * n
        ax.hlines(y, rangos.iloc[a] - 0.03, rangos.iloc[b] + 0.03, color="black", lw=3)

    if titulo:
        ax.set_title(titulo, fontsize=10)
    fig.tight_layout()
    if ruta:
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(ruta, dpi=300, bbox_inches="tight")
        fig.savefig(Path(ruta).with_suffix(".svg"), bbox_inches="tight")
    return fig


def holm(p_valores):
    """Corrección de Holm-Bonferroni. Devuelve los p-valores ajustados en el mismo orden."""
    p = np.asarray(p_valores, dtype=float)
    orden = np.argsort(p)
    m = len(p)
    ajustados = np.empty(m)
    maximo = 0.0
    for posicion, i in enumerate(orden):
        maximo = max(maximo, (m - posicion) * p[i])
        ajustados[i] = min(1.0, maximo)
    return ajustados


def wilcoxon_holm(M, mayor_es_mejor=True, alpha=0.05):
    """Wilcoxon de rangos con signo para cada par de modelos, con corrección de Holm."""
    filas = []
    for a, b in combinations(M.columns, 2):
        dif = M[a] - M[b]
        if np.allclose(dif, 0):
            est, p = np.nan, 1.0
        else:
            est, p = stats.wilcoxon(M[a], M[b], zero_method="zsplit")
        mejor = a if (dif.median() > 0) == mayor_es_mejor else b
        filas.append({"modelo_a": a, "modelo_b": b, "mediana_diferencia_a_menos_b": float(dif.median()),
                      "estadistico_W": est, "p_valor": float(p), "mejor_segun_mediana": mejor})
    tabla = pd.DataFrame(filas)
    tabla["p_holm"] = holm(tabla["p_valor"])
    tabla["diferencia_significativa"] = tabla["p_holm"] < alpha
    return tabla.sort_values("p_holm").reset_index(drop=True)


def reporte_texto(fr, cd, alpha=0.05):
    """Frase lista para adaptar en el documento (revisa y redacta con tus palabras)."""
    decision = "se rechaza" if fr["p_valor"] < alpha else "no se rechaza"
    mejor = fr["rangos_promedio"].index[0]
    return (f"La prueba de Friedman (χ² = {fr['estadistico']:.2f}, k = {fr['k_modelos']}, "
            f"N = {fr['n_bloques']} particiones, p = {fr['p_valor']:.4f}) indica que {decision} la hipótesis "
            f"de igual desempeño entre los modelos (α = {alpha}). El mejor rango promedio fue {mejor} "
            f"({fr['rangos_promedio'].iloc[0]:.2f}); la diferencia crítica de Nemenyi es CD = {cd:.2f}.")


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    rng = np.random.default_rng(42)
    filas = []
    for modelo, base in [("Línea base", 0.60), ("Logística", 0.90), ("Random Forest", 0.92), ("SVM", 0.91)]:
        for i in range(10):
            filas.append({"modelo": modelo, "repeticion": i // 5 + 1, "pliegue": i % 5 + 1,
                          "metrica": "f1_macro", "valor": base + rng.normal(0, 0.02)})
    M = matriz_desempeno(pd.DataFrame(filas), "f1_macro")
    fr = friedman(M)
    cd = nemenyi(fr["rangos_promedio"], fr["n_bloques"])
    print(reporte_texto(fr, cd))
    print(wilcoxon_holm(M).round(4))
    diagrama_diferencia_critica(fr["rangos_promedio"], cd, "results_demo/figures/diferencia_critica.png")

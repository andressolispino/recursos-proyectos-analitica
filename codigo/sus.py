"""Puntaje SUS (System Usability Scale) para evaluar la usabilidad de un tablero.

Cada usuario responde 10 afirmaciones de 1 (totalmente en desacuerdo) a 5 (totalmente de acuerdo)
después de resolver 2 o 3 tareas con el tablero. Las afirmaciones están en el prompt 22.

Cálculo (Brooke, 1996): en los ítems impares se resta 1 al valor; en los pares se resta el valor a 5;
se suman los 10 resultados y se multiplica por 2,5 (escala de 0 a 100). La referencia habitual es 68.

Uso:
    import pandas as pd
    from sus import puntaje_sus, resumen_sus
    respuestas = pd.read_csv("sus_respuestas.csv")   # columnas p1 … p10, una fila por usuario, sin nombres
    puntajes = puntaje_sus(respuestas)
    print(resumen_sus(puntajes))

Referencias: Brooke, J. (1996). SUS: A "quick and dirty" usability scale. En Usability Evaluation in
Industry (pp. 189–194). Taylor & Francis. Bangor, Kortum y Miller (2009) proponen la escala de adjetivos.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

COLUMNAS = [f"p{i}" for i in range(1, 11)]


def puntaje_sus(respuestas):
    """Devuelve una Serie con el puntaje SUS (0–100) de cada usuario."""
    faltan = [c for c in COLUMNAS if c not in respuestas.columns]
    if faltan:
        raise ValueError(f"Faltan columnas: {faltan}. Se esperan p1 a p10.")
    r = respuestas[COLUMNAS].astype(float)
    if ((r < 1) | (r > 5)).any().any() or r.isna().any().any():
        raise ValueError("Todas las respuestas deben estar entre 1 y 5, sin vacíos.")
    impares = (r[["p1", "p3", "p5", "p7", "p9"]] - 1).sum(axis=1)
    pares = (5 - r[["p2", "p4", "p6", "p8", "p10"]]).sum(axis=1)
    return ((impares + pares) * 2.5).rename("puntaje_sus")


def resumen_sus(puntajes, alpha=0.05, referencia=68.0):
    """Media, desviación estándar, IC del 95 % (t) y comparación con la referencia de 68 puntos."""
    p = np.asarray(puntajes, dtype=float)
    n = len(p)
    media, de = p.mean(), p.std(ddof=1) if n > 1 else 0.0
    res = {"usuarios": n, "media": round(float(media), 1), "de": round(float(de), 1)}
    if n >= 2:
        t = stats.t.ppf(1 - alpha / 2, n - 1)
        res["ic95"] = (round(float(media - t * de / np.sqrt(n)), 1), round(float(media + t * de / np.sqrt(n)), 1))
    res["frente_a_68"] = "por encima" if media > referencia else "por debajo o igual"
    if n < 5:
        res["advertencia"] = "Menos de 5 usuarios: el resultado es solo indicativo."
    return res


if __name__ == "__main__":
    ejemplo = pd.DataFrame([   # respuestas ficticias, solo para probar el cálculo
        [4, 2, 4, 1, 4, 2, 5, 1, 4, 2],
        [5, 1, 5, 2, 4, 1, 4, 2, 5, 1],
        [3, 3, 4, 2, 3, 2, 4, 2, 3, 3],
        [4, 2, 5, 1, 4, 2, 4, 1, 4, 2],
        [4, 1, 4, 2, 5, 1, 5, 1, 4, 2],
    ], columns=COLUMNAS)
    s = puntaje_sus(ejemplo)
    print(s.tolist())
    print(resumen_sus(s))
    assert s.iloc[0] == 82.5

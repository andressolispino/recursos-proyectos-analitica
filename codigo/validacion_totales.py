"""Validación de totales contra la fuente (enfoque descriptivo: modelo dimensional, KPI y tablero).

Compara, para cada tabla de hechos o KPI, el número de registros y los totales de control (sumas,
conteos o conteos de distintos) entre la fuente original y tu modelo o tablero. La diferencia
esperada es cero; si no lo es, el informe debe explicar por qué (filtros, deduplicación, periodo…).

Uso:
    from validacion_totales import validar_totales
    controles = {
        "Registros": ("conteo", None),
        "Ventas totales": ("suma", "valor_venta"),
        "Clientes distintos": ("distintos", "id_cliente"),
    }
    tabla = validar_totales(df_fuente, df_hechos, controles, nombre="hechos_ventas")

Guarda results/tables/validacion_totales_<nombre>.csv.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

OPERACIONES = {
    "conteo": lambda df, col: len(df),
    "suma": lambda df, col: df[col].sum(),
    "distintos": lambda df, col: df[col].nunique(),
    "media": lambda df, col: df[col].mean(),
}


def validar_totales(fuente, modelo, controles, nombre="modelo", tolerancia=1e-9, carpeta="results",
                    columnas_modelo=None):
    """controles: {"Etiqueta": (operación, columna_en_fuente)} con operación en conteo/suma/distintos/media.

    columnas_modelo: {"columna_en_fuente": "columna_en_modelo"} si se renombraron en el modelo.
    """
    columnas_modelo = columnas_modelo or {}
    filas = []
    for etiqueta, (op, col) in controles.items():
        if op not in OPERACIONES:
            raise ValueError(f"Operación desconocida: {op}")
        v_fuente = OPERACIONES[op](fuente, col)
        v_modelo = OPERACIONES[op](modelo, columnas_modelo.get(col, col))
        dif = float(v_modelo) - float(v_fuente)
        pct = (dif / float(v_fuente) * 100) if v_fuente else np.nan
        filas.append({"control": etiqueta, "operacion": op, "columna": col,
                      "fuente": v_fuente, "modelo": v_modelo, "diferencia": dif,
                      "diferencia_pct": pct, "coincide": abs(dif) <= tolerancia * max(1.0, abs(float(v_fuente)))})
    tabla = pd.DataFrame(filas)
    Path(carpeta, "tables").mkdir(parents=True, exist_ok=True)
    tabla.to_csv(Path(carpeta, "tables", f"validacion_totales_{nombre}.csv"), index=False)
    if not tabla["coincide"].all():
        print("⚠ Hay controles que no coinciden: explica la causa en el documento.")
    return tabla


if __name__ == "__main__":
    fuente = pd.DataFrame({"id_cliente": [1, 2, 2, 3, 4], "valor_venta": [10.0, 20.0, 20.0, 5.0, 7.5]})
    hechos = fuente.drop_duplicates()        # el modelo eliminó un duplicado
    print(validar_totales(fuente, hechos, {"Registros": ("conteo", None),
                                           "Ventas totales": ("suma", "valor_venta"),
                                           "Clientes distintos": ("distintos", "id_cliente")},
                          nombre="demo", carpeta="results_demo").to_string())

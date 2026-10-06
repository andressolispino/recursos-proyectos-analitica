"""Resume la estructura de un CSV sin exportar filas ni valores de columnas.

Uso: python generar_insumos_ia.py datos.csv --excluir nombre correo documento
Revisa el archivo generado antes de compartirlo con una herramienta externa.
"""
from pathlib import Path
import argparse
import pandas as pd


def generar_insumos(df, columnas_excluidas=()):
    """Devuelve tipos, conteos y porcentajes; no incluye muestras ni categorías."""
    datos = df.drop(columns=list(columnas_excluidas), errors="ignore")
    esquema = pd.DataFrame({
        "tipo": datos.dtypes.astype(str),
        "no_nulos": datos.notna().sum(),
        "faltantes_porcentaje": (datos.isna().mean() * 100).round(2),
        "valores_distintos_conteo": datos.nunique(dropna=True),
    })
    return "\n\n".join([
        "RESUMEN DE ESTRUCTURA — REVISAR ANTES DE COMPARTIR",
        f"Forma: {len(datos)} filas x {len(datos.columns)} columnas",
        "== Esquema y calidad por columna ==\n" + esquema.to_string(),
        "No se incluyeron filas, categorías ni valores numéricos originales.",
        "Los nombres de columnas y los conteos también pueden ser confidenciales. "
        "Excluir columnas no garantiza anonimización; revisa el resultado.",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", type=Path)
    parser.add_argument("--excluir", nargs="*", default=[])
    parser.add_argument("--salida", type=Path, default=Path("insumos_ia.txt"))
    args = parser.parse_args()
    df = pd.read_csv(args.csv)
    args.salida.write_text(generar_insumos(df, args.excluir), encoding="utf-8")
    print(f"Guardado: {args.salida}. Revísalo antes de compartirlo.")


if __name__ == "__main__":
    main()

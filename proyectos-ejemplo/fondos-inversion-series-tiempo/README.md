# Pronóstico de los activos administrados por los fondos de inversión colectiva (FIC) en Colombia

Trabajo de grado de especialización en analítica de datos (enfoque predictivo, pronóstico de una serie de tiempo diaria). Compartido con autorización de su autor; se retiraron los nombres y las rutas personales.

**Variable objetivo:** `AUM FIC`, el valor diario de los activos administrados por los fondos de inversión colectiva, desde 2018, junto con variables macroeconómicas (inflación, tasa de política monetaria, agregados monetarios y bonos TES).

La particularidad de este proyecto es que **cada modelo tiene su propio cuaderno**, lo que facilita compararlos y ver cómo se prepara la serie para cada familia de modelos.

## Orden de los cuadernos

| # | Cuaderno | Qué hace | Etapa de la [ruta](../../guias/ruta-del-proyecto.md) |
| --- | --- | --- | --- |
| 2 | [02_data_unification.ipynb](02_data_unification.ipynb) | Une las fuentes en una sola tabla: valor diario de los fondos (consultado desde una base MySQL local con datos de la Superintendencia Financiera), rentabilidades de los FIC (datos.gov.co), IPC, TES (COLTES), agregados monetarios y tasa de política monetaria (archivos del Banco de la República). | 1 y 2 |
| 1 | [01_eda_sarima.ipynb](01_eda_sarima.ipynb) | EDA de la serie (tendencia, estacionalidad por año y mes, medias móviles), modelos SARIMA y modelado de la volatilidad con GARCH (`arch`). | 2 y 3 |
| 3 | [03_autoregressive.ipynb](03_autoregressive.ipynb) | Relación entre variables (correlación de Spearman), estacionariedad (ADF) y diferenciación, causalidad de Granger y modelos autorregresivos: ARIMA, VAR y GARCH. | 3 |
| 5 | [05_exp_smoothing.ipynb](05_exp_smoothing.ipynb) | Suavizado exponencial simple y Holt-Winters con tendencia y estacionalidad multiplicativas. | 3 |
| 6 | [06_lstm.ipynb](06_lstm.ipynb) | Red LSTM con partición entrenamiento/validación/prueba (80/10/10), escalado, conjuntos supervisados y ajuste con `keras_tuner`. | 3 |
| 7 | [07_lightgbm.ipynb](07_lightgbm.ipynb) | LightGBM, CatBoost e `HistGradientBoosting` con `skforecast`: rezagos elegidos con la PACF calculada solo sobre entrenamiento, variables de calendario, búsqueda bayesiana de hiperparámetros, *backtesting* y explicabilidad con SHAP. | 3 y 4 |
| 8 | [08_xgboost.ipynb](08_xgboost.ipynb) | XGBoost con `skforecast` (pronóstico recursivo y directo), primero solo con la variable objetivo y luego con exógenas; búsqueda de hiperparámetros, *backtesting* y explicabilidad con SHAP. | 3 y 4 |
| 9 | [09_prophet.ipynb](09_prophet.ipynb) | Prophet. | 3 |
| 10 | [10_moving_avg_baseline.ipynb](10_moving_avg_baseline.ipynb) | Línea base de media móvil, el punto de comparación de todos los modelos. | 3 |

La numeración original salta del 3 al 5. El cuaderno 2 produce el archivo que usan los demás, así que conviene leerlo primero.

## Datos y ejecución

- Los cuadernos leen `BD preprocesada II.csv`, que **no** está en este repositorio. El cuaderno 2 genera `BD completa.csv` y `BD preprocesada I.csv` a partir de las fuentes indicadas arriba; la versión II es la depuración final que usan los modelos.
- El cuaderno 2 se conecta a una base de datos MySQL local del autor; para reproducirlo debes cargar los datos de la Superintendencia Financiera en tu propia base o adaptar la lectura a archivos CSV.
- Los cuadernos 7 y 8 importan un módulo local `config` que no forma parte del material compartido; reemplaza esas líneas por tus propias rutas y parámetros.
- Se ejecutaron en un equipo local con Python 3.12, no en Colab.

## Qué mirar con ojo crítico

- **Comparación justa:** ¿todos los modelos usan la misma partición y la misma métrica? Compara cada uno contra la línea base de media móvil (cuaderno 10).
- **Fuga de información:** el cuaderno 7 elige los rezagos con la PACF solo sobre entrenamiento; revisa si los demás cuadernos hacen lo mismo con el escalado y la selección de variables.
- **Rigor:** ¿hay validación temporal repetida, intervalos de confianza y prueba estadística entre modelos? Puedes completarlo con el [código de apoyo](../../codigo/README.md) y la [lista de chequeo del Hito 3](../../guias/hito-3-resultados-y-discusion.md).

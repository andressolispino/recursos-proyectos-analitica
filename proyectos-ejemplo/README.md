# Proyectos de ejemplo

Cuadernos completos de dos trabajos de grado reales de posgrado en analítica de datos, compartidos con autorización de sus autores con fines educativos. Se retiraron los nombres, los datos de las cuentas de Colab y las rutas personales.

Sirven para ver **cómo se ve un proyecto terminado de punta a punta**: de dónde salen los datos, cómo se limpian y exploran, cómo se comparan modelos y cómo se reportan las métricas. Los cuadernos conservan sus salidas (tablas y figuras), así que se pueden leer en GitHub sin ejecutarlos.

| Proyecto | Tipo de problema | Qué muestra |
| --- | --- | --- |
| [Demanda de energía eléctrica](demanda-energia-regresion/README.md) | Regresión y series de tiempo (horarias) | Consolidación de varias fuentes por API (XM, NASA POWER, datos.gov.co), EDA, ARIMA/SARIMA/SARIMAX y una batería de modelos de *machine learning* con selección de variables y ajuste de hiperparámetros |
| [Activos de fondos de inversión colectiva](fondos-inversion-series-tiempo/README.md) | Pronóstico de series de tiempo (diarias) | Unificación de fuentes financieras, SARIMA/GARCH, suavizado exponencial, LSTM, LightGBM, XGBoost, Prophet y una línea base de media móvil, un cuaderno por modelo |

## Cómo usarlos

- **Para leer:** abre cualquier cuaderno en GitHub. Si no se muestra (a veces pasa con cuadernos grandes), pega su dirección en [nbviewer.org](https://nbviewer.org/).
- **Para ejecutar en Colab:** cambia `github.com` por `colab.research.google.com/github` en la dirección del cuaderno. Necesitarás los datos de cada proyecto (ver su README) y ajustar las rutas, que apuntan al Google Drive o al equipo de sus autores.
- **Para aprender de ellos:** compáralos con la [ruta del proyecto](../guias/ruta-del-proyecto.md) y con las listas de chequeo de los hitos. Son trabajos reales, con aciertos y con cosas por mejorar: busca dónde aplican bien la validación temporal y dónde podría haber fuga de información, qué línea base usan y cómo reportan la incertidumbre. Es un buen ejercicio de lectura crítica antes de construir tu propio proyecto.

> Si reutilizas código de estos cuadernos, entiéndelo y cítalo en tu documento como «Proyecto de ejemplo del repositorio *Recursos para proyectos y tesis de analítica de datos*».

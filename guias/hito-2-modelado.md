# Hito 2: desarrollo y modelado

Estas orientaciones son adaptables; no constituyen una rúbrica ni reemplazan las indicaciones de tu director. Justifica cada técnica y ajusta la cantidad de modelos, las particiones y las variantes al problema.

## 1. Dónde estás en la ruta

En este hito trabajas las **etapas 2 y 3** de la [Ruta del proyecto](ruta-del-proyecto.md): ingeniería de características (feature engineering) y modelado, con entrenamiento de línea base y optimización de modelos, o modelado dimensional, KPIs y dashboard si tu enfoque es descriptivo.

## 2. Qué vas a lograr

**Propósito.** Ejecutar la ingeniería de características y el modelado de tu proyecto con un diseño comparativo riguroso. Comparar varios modelos en las mismas condiciones es lo que te permite elegir el mejor con argumentos y mejorar tu trabajo.

**Resultado de aprendizaje.** Organiza, procesa y analiza la información con técnicas pertinentes y coherentes con el diseño metodológico.

## 3. Recursos para este hito

- [Plantilla general de documento](../plantillas/documento-de-investigacion.md)
- [Cómo entregar el código (Colab y GitHub)](colab-y-github.md): cómo subir tus avances y crear la versión v0.2 desde la página de GitHub. ¿Primera vez en GitHub? Esa guía tiene dos videos tutoriales en español y el enlace a la [documentación oficial de GitHub](https://docs.github.com/es/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
- **Código de apoyo del repositorio:** [bateria_modelos.py](../codigo/bateria_modelos.py) evalúa todos tus modelos con la misma validación repetida y genera `metricas_por_particion.csv`, `resumen_modelos.csv` y `experiments.csv`; [validacion_totales.py](../codigo/validacion_totales.py) concilia los totales de tu modelo dimensional o tablero contra la fuente. Míralos funcionando en el [cuaderno de flujo completo](../notebooks/01_flujo_rigor_analitico.ipynb).
- [Guía de prompts de IA](../prompts/README.md): prompts listos para proponer variables, auditar tu código contra la fuga de información, programar la batería de modelos con validación repetida, optimizar con Optuna, resolver errores e interpretar resultados (prompts 9 a 15), y prompts de revisión para convertir la retroalimentación del Hito 1 en un plan de ajustes (R12) y revisar tu metodología, tu desarrollo y tu repositorio (R5, R6 y R11).
- [Tablas y figuras sugeridas (opcional)](../plantillas/tablas-y-figuras.md): incluye las tablas de resultados, hiperparámetros y ablación.
- [Normas APA](escritura-y-referencias.md) · [Escritura y referencias](escritura-y-referencias.md)
- **Códigos de ayuda por tema**: ejemplos reales en GitHub para cada paso de este hito. 

  | Tema de la ruta | Ejemplos en GitHub (cuadernos de proyectos reales) |
  | --- | --- |
  | **Etapa 2 · Ingeniería de características** | - [Rezagos](https://github.com/Ameen2488/time-series-feature-engineering/blob/main/notebooks/06_lag_features.ipynb) y [ventanas móviles](https://github.com/Ameen2488/time-series-feature-engineering/blob/main/notebooks/07_window_features.ipynb)<br>- [Variables de rezago y ventana sin fuga](https://github.com/sidharthmenon626-lab/demand-forecasting-ml/blob/main/notebooks/02_features.ipynb)<br>- [Variables de calendario y LightGBM](https://github.com/agrawalvanshika/Hourly-Energy-Consumption/blob/main/Notebooks/03_Feature_Engineering_and_LightGBM.ipynb) |
  | **Etapa 2 · Selección de variables** | - [Boruta, RFE, información mutua y Lasso](https://github.com/trizkynoviandy/feature-selection-guide/blob/main/fs_guide.ipynb)<br>- [RFE, Lasso y SelectKBest en un caso real](https://github.com/nic-stack/DAV6150-Data-Science-Portfolio/blob/main/02-feature-selection-news-popularity/news_popularity_feature_selection.ipynb) |
  | **Etapa 3 · Validación sin fuga y desbalance** | - [Pipeline con TimeSeriesSplit para evitar fuga](https://github.com/Ameen2488/time-series-feature-engineering/blob/main/notebooks/02_ml_pipeline_leakage.ipynb)<br>- [SMOTE aplicado solo en entrenamiento](https://github.com/kohjiaxuan/Fraud-Detection-Pipeline/blob/master/OVER02.%20Model%20building%20with%20naive%20sample%20and%20SMOTE.ipynb)<br>- [SMOTE, ensambles de votación y apilamiento](https://github.com/Ruchadhage/customer-churn-using-shap-explainability/blob/master/customer_churn.ipynb) |
  | **Etapa 3 · Batería de modelos** | - [Regresión logística, SVM, Random Forest y XGBoost con pipelines](https://github.com/ShienTioh/Machine-Learning-Model-Comparison/blob/main/notebooks/COGS_118A_model_comparison.ipynb)<br>- [Cinco clasificadores comparados en cuatro datasets](https://github.com/kshtwr/Evaluating-Classifiers/blob/main/Final%20Project%20Code.ipynb)<br>- [Modelado predictivo y validación](https://github.com/JDAG-SUP/mineria-de-datos-jd-y-dm/blob/main/notebooks/02_Modelado_Predictivo.ipynb) (en español)<br>- [Batería de modelos de regresión con particiones 80-20 y 90-10 y análisis comparativo](../proyectos-ejemplo/demanda-energia-regresion/README.md), cuadernos 2, 2.1, 2.2 y 2.4 (proyecto de ejemplo de este repositorio, en español) |
  | **Etapa 3 · Optimización de hiperparámetros** | - [XGBoost optimizado con Optuna](https://github.com/ghanmi-hamza/Hyperparameter_Tuning_Using_Optuna/blob/master/xgboost-hyperparameter-tuning-using-optuna.ipynb)<br>- [Un cuaderno por modelo de árboles con búsqueda de hiperparámetros](https://github.com/TAMIM-IQBAL0110/tree-based-ml-and-hyperparameter-tuning)<br>- [Ajuste de hiperparámetros con GridSearchCV y validación temporal](../proyectos-ejemplo/demanda-energia-regresion/02_3_ajuste_hiperparametros_80_20.ipynb) (proyecto de ejemplo de este repositorio, en español) |
  | **Etapa 3 · Modelos para series de tiempo** | - [Línea base, LightGBM, comparación final y LSTM](https://github.com/agrawalvanshika/Hourly-Energy-Consumption/tree/main/Notebooks)<br>- [EDA, preprocesamiento, SARIMA y LSTM](https://github.com/AravindLN123/Energy-Demand-Forecasting-SARIMA-LSTM-/tree/main/Code)<br>- [XGBoost y CatBoost con rezagos](https://github.com/jorgegalanr/energy-forecasting-xgboost-catboost/blob/main/notebooks/energy_forecasting.ipynb)<br>- [Proyecto completo de pronóstico de series de tiempo: fondos de inversión colectiva](../proyectos-ejemplo/fondos-inversion-series-tiempo/README.md) (proyecto de ejemplo de este repositorio, en español): un cuaderno por modelo: unificación de datos, EDA y SARIMA, modelos autorregresivos, suavizado exponencial, LSTM, LightGBM, XGBoost, Prophet y línea base de media móvil. |
  | **Etapa 3 · Enfoque descriptivo: modelo dimensional, KPIs y dashboard** | - [ETL a un esquema estrella (dimensiones y hechos)](https://github.com/tayssermahmoud4-del/central-superstore-data-warehouse/blob/main/notebooks/etl_load_to_sql_server.ipynb)<br>- [Limpieza, KPIs, RFM y dashboard en Streamlit](https://github.com/dgh19981102-max/ecommerce-sales-analytics-dashboard)<br>- [Esquema estrella con SQL, Python y Power BI](https://github.com/Franchutech/sql-star-schema-retail) |

  Son repositorios de otros estudiantes y analistas (la mayoría en inglés). Ábrelos para ver cómo resolvieron cada paso y adapta las ideas a tus datos. Para ejecutar un cuaderno en Colab, cambia `github.com` por `colab.research.google.com/github` en su dirección. Si reutilizas código ajeno, entiéndelo y cítalo en tu documento.
- Todo lo anterior también está en la sección [Catálogo de ejemplos de código](../recursos/ejemplos-de-codigo.md).
- Para profundizar: [scikit-learn, errores comunes y fuga de información](https://scikit-learn.org/stable/common_pitfalls.html); [imbalanced-learn, errores comunes](https://imbalanced-learn.org/stable/common_pitfalls.html); [Kaggle Learn, cursos Feature Engineering e Intermediate Machine Learning](https://www.kaggle.com/learn); [TensorFlow, pronóstico de series de tiempo con LSTM](https://www.tensorflow.org/tutorials/structured_data/time_series); [Optuna](https://optuna.org/); [Nixtla NeuralForecast](https://nixtlaverse.nixtla.io/neuralforecast/docs/getting-started/introduction.html).

**⚠ Sobre el uso de IA:** úsala como lo hace un analista profesional, para programar, depurar, verificar y revisar. Pero **redacta tú**, con tus palabras; **entiende** cada línea de código, cada modelo y cada métrica, y **no copies** respuestas tal cual. **El jurado te va a preguntar** por qué elegiste esos modelos y esa validación, y en la sustentación no hay IA.

## 4. Qué entregas

1. **Implementación de ajustes del Hito 1.** Requisito indispensable: aplica todas las correcciones de la retroalimentación del Hito 1 antes de añadir contenido nuevo.
2. **Desarrollo de los nuevos objetivos** (continuación del capítulo de desarrollo del proyecto). Desarrolla el objetivo específico 2 y, si tu proyecto tiene cuatro objetivos, también el 3. Describe el diseño (cómo lo haces y por qué) y documenta la ejecución, la evidencia y los resultados.
3. **Disponibilidad de datos y código.** Actualiza esa sección del documento.
4. **Declaración de uso de IA.** Actualízala.

## 5. Lista de chequeo técnica (sugerida)

- ☐ **Ingeniería de características:** tabla con cada variable creada (nombre, fórmula y justificación). Incluye variables del dominio y, si hay fechas, rezagos, ventanas móviles y variables de calendario; codificación de categóricas y escalado. Aplica un método de selección (información mutua, RFE, LASSO o Boruta) o de reducción (PCA) e indica qué variables quedaron.
- ☐ **Partición y validación según el protocolo definido antes de modelar:** separa el conjunto de prueba antes de cualquier transformación. Usa validación cruzada repetida y estratificada (por ejemplo, 5×2 o 10×3 con `RepeatedStratifiedKFold`) o, si hay fechas, validación temporal (`TimeSeriesSplit` con al menos 5 cortes). Repetir la validación hace que la comparación entre modelos sea más confiable. Todo el preprocesamiento va dentro de un Pipeline, y el balanceo de clases (pesos de clase o SMOTE) solo dentro de entrenamiento. Fija la semilla.
- ☐ **Batería de modelos, de menor a mayor complejidad:** (a) línea base ingenua y un modelo clásico (regresión lineal o logística; ARIMA o SARIMA en series); (b) convencionales: Ridge o Lasso, KNN, SVM y árbol de decisión; (c) ensambles: Random Forest y al menos uno de XGBoost, LightGBM o CatBoost; (d) redes neuronales: MLP, y LSTM o GRU si los datos son secuenciales.
- ☐ **Optimización de hiperparámetros** con Optuna u otra búsqueda, sobre validación y nunca sobre prueba, con el mismo número de pruebas para todos los modelos; incluye una tabla con el espacio de búsqueda y los mejores valores.
- ☐ **Métricas:** en regresión RMSE, MAE, MAPE y R²; en clasificación F1-macro, AUC-ROC, AUC-PR, MCC y matriz de confusión. Reporta la media ± desviación estándar entre particiones, el tiempo de entrenamiento y el resultado en prueba de cada modelo, con una figura que compare todos los modelos y otra del mejor (real contra predicho y residuos, o matriz de confusión y curva ROC). Guarda las tablas en CSV en results/tables. Guarda además la métrica principal de cada modelo en cada partición en `results/tables/metricas_por_particion.csv` (una fila por modelo y partición): con ese archivo harás la prueba estadística y los intervalos de confianza del Hito 3.
- ☐ **Ablación:** compara el mejor modelo con y sin la ingeniería de características. En el Hito 3 la amplías a una tabla de ablación completa.
- ☐ **Si tu enfoque es descriptivo:** modelo dimensional (hechos y dimensiones), KPIs con fórmula y dashboard funcional con capturas, además de la ingeniería de características.
- ☐ **Si tu enfoque es descriptivo: validación de totales contra la fuente.** Una tabla que compare, para cada tabla de hechos y para cada KPI principal, el número de registros y los totales de control (sumas o conteos) en la fuente original y en tu modelo o tablero. La diferencia esperada es cero; si no lo es, explica por qué. Apóyate en el prompt 15 de la guía de prompts.
- ☐ **Trazabilidad:** bitácora de decisiones actualizada, archivo results/experiments.csv con una fila por corrida (fecha, modelo, parámetros, semilla y métricas) y repositorio con la versión v0.2.
- ☐ **Reglas de reporte:** las mismas del Hito 1: títulos que se entiendan solos, interpretación debajo de cada figura y tabla, y ninguna cifra escrita a mano.
- ☐ **Formato:** el mismo PDF del Hito 1 ya corregido (no empieces un archivo nuevo), en el formato establecido por tu programa y con APA 7. Extensión y soportes según tu programa. Evidencias recomendadas: cuaderno de Colab y repositorio con la versión v0.2.

## 6. Ideas para profundizar (opcionales)

Elige las ideas que aporten a tu pregunta y acuerda su alcance con tu director. Su utilidad depende del tipo de proyecto y de los datos disponibles.

| Idea | Qué hacer en este hito | Por qué mejora tu trabajo |
| --- | --- | --- |
| **Compara alternativas** | Prueba un método más avanzado que los ya comparados, o una combinación de tus mejores modelos (por votación o apilamiento), y compáralo en las mismas condiciones: mismas particiones y misma métrica. | Muestras si la complejidad extra de verdad mejora el resultado. |
| **Demuestra que se sostiene** | Repite la evaluación cambiando la semilla o la forma de partir los datos y revisa si el orden de los modelos se mantiene. | Un resultado que se repite es un resultado en el que se puede confiar. |
| **Suma contexto** | Quita un grupo de variables a la vez (por ejemplo, las de fecha o las de lugar) y mide cuánto cambia la métrica. | Sabes qué información es la que realmente explica el resultado. |
| **Tradúcelo a decisiones** | Explica qué significa la métrica del mejor modelo en el problema, por ejemplo «de cada 100 casos, identifica 87» o «se equivoca en promedio en X unidades». | Cualquier lector entiende el valor de tu modelo. |

[Volver al inicio](../README.md)

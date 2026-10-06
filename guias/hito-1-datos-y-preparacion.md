# Hito 1: formulación, datos y preparación

Estas orientaciones son adaptables; no constituyen una rúbrica ni reemplazan las indicaciones de tu director. Justifica cada técnica y ajusta la cantidad de modelos, las particiones y las variantes al problema.

## 1. Dónde estás en la ruta

En este hito trabajas las **etapas 1 y 2** de la [Ruta del proyecto](ruta-del-proyecto.md): problema de negocio, estado del arte y adquisición de datos (etapa 1), y proceso ETL/ELT y EDA multivariado (primera parte de la etapa 2).

## 2. Qué vas a lograr

Damos el salto de la planificación a la ejecución. Trabajarás sobre un único documento que evolucionará durante todo el periodo. Cada requisito técnico que te pedimos está pensado para mejorar tu trabajo: que quede sólido, que se pueda reproducir y que puedas defenderlo con seguridad ante los jurados.

**Propósito.** Dejar el anteproyecto reescrito y listo para ejecutar, los datos adquiridos y documentados, y el objetivo específico 1 cumplido.

**Resultado de aprendizaje.** Ajusta y ejecuta la ruta metodológica del proyecto, y organiza y procesa la información con técnicas pertinentes.

## 3. Recursos para este hito

- [Plantilla general de documento](../plantillas/documento-de-investigacion.md)
- [Cómo entregar el código (Colab y GitHub)](colab-y-github.md): paso a paso para subir tu código y crear la versión v0.1 desde la página de GitHub. ¿Primera vez en GitHub? Esa guía tiene dos videos tutoriales en español y el enlace a la [documentación oficial de GitHub](https://docs.github.com/es/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
- **Proyecto de ejemplo completo:** [consolidación de varias fuentes por API y EDA](../proyectos-ejemplo/demanda-energia-regresion/README.md) en un trabajo de grado real, y el [script de insumos para IA](../codigo/generar_insumos_ia.py) para describir tus datos sin compartirlos.
- [Guía de prompts de IA](../prompts/README.md): prompts listos para afinar tu pregunta, evaluar el dataset, descargar datos de datos.gov.co, armar el diccionario, planear la limpieza y el EDA, y fijar tu protocolo de evaluación (prompts 1 a 8), y prompts para revisar tus capítulos con criterios de jurado (R1 a R6). Cada prompt ya trae tu bloque de contexto y te dice qué adjuntar.
- [Tablas y figuras sugeridas (opcional)](../plantillas/tablas-y-figuras.md): ideas de tablas y figuras para tu documento.
- [Normas APA](escritura-y-referencias.md) · [Escritura y referencias](escritura-y-referencias.md)
- **Códigos de ayuda por tema**: ejemplos reales en GitHub para cada paso de este hito. 

  | Tema de la ruta | Ejemplos en GitHub (cuadernos de proyectos reales) |
  | --- | --- |
  | **Etapa 1 · Conectarte a datos.gov.co (API)** | - [Consulta de datos.gov.co con sodapy](https://github.com/ANCP-CCE-Analitica/datos_abiertos/blob/main/SOCRATA_Consulta.ipynb) (en español)<br>- [Tutorial: conectarse a la API de resultados del Icfes](https://ccamilocristian.github.io/posts/icfes-conexion-api/) (en español)<br>- [Aplicación de EDA para datasets de datos.gov.co](https://github.com/MPalma21/eda-colombia-shiny) |
  | **Etapa 2 · Limpieza y ETL** | - [ETL paso a paso con pandas](https://github.com/Miinaaann/ETL-Pandas/blob/main/01_ETL_Sensor_Data_Tutorial.ipynb)<br>- [Limpieza con faltantes, duplicados y atípicos (IQR)](https://github.com/JanarthanKumar/Data-Cleaning-Visualization-Project/blob/main/Data%20Cleaning%20%26%20Visualization%20Project.ipynb)<br>- [Limpieza de datos](https://github.com/sebastian2509052-cmd/analisis_exploratorio/blob/main/1_limpieza_de_datos.ipynb) (en español)<br>- [Consolidación de varias fuentes en un solo dataset (APIs de XM, NASA POWER y datos.gov.co)](../proyectos-ejemplo/demanda-energia-regresion/00_consolidacion_dataset.ipynb) (proyecto de ejemplo de este repositorio, en español) |
  | **Etapa 2 · EDA univariado y bivariado** | - [EDA completo de un dataset](https://github.com/sebastian2509052-cmd/analisis_exploratorio/blob/main/2_eda_imdb.ipynb) (en español)<br>- [EDA y selección de factores](https://github.com/JDAG-SUP/mineria-de-datos-jd-y-dm/blob/main/notebooks/01_EDA_Seleccion_Factores.ipynb) (en español)<br>- [Exploración del dataset y preparación por familia de modelos](../proyectos-ejemplo/demanda-energia-regresion/01_exploracion_dataset.ipynb) (proyecto de ejemplo de este repositorio, en español) |
  | **Etapa 2 · EDA multivariado** | - [Correlaciones, chi-cuadrado y análisis por subgrupos](https://github.com/SaharSun/Heart_Disease-eda/blob/main/Heart_Disease.ipynb)<br>- [Multicolinealidad con VIF](https://github.com/aayushi-droid/Multicollinearity-in-Regression-Analysis/blob/master/Multicollinearity%20Notebook.ipynb)<br>- [Correlación y VIF en un caso de precios](https://github.com/LAXMI15PRIYA/house-price-prediction/blob/main/notebooks/house_price_analysis.ipynb) |
  | **Etapa 2 · EDA cuando hay fechas** | - [Tendencia y estacionalidad en demanda de energía](https://github.com/agrawalvanshika/Hourly-Energy-Consumption/blob/main/Notebooks/01_Data_Loading_and_Exploratory_Data_Analysis.ipynb)<br>- [Descomposición de una serie de tiempo](https://github.com/Ameen2488/time-series-feature-engineering/blob/main/notebooks/03_decomposition.ipynb) |

  Son repositorios de otros estudiantes y analistas (la mayoría en inglés). Ábrelos para ver cómo resolvieron cada paso y adapta las ideas a tus datos. Para ejecutar un cuaderno en Colab, cambia `github.com` por `colab.research.google.com/github` en su dirección. Si reutilizas código ajeno, entiéndelo y cítalo en tu documento.
- Todo lo anterior también está en la sección [Catálogo de ejemplos de código](../recursos/ejemplos-de-codigo.md).
- Para profundizar: [Manual del desarrollador de datos.gov.co](https://herramientas.datos.gov.co/sites/default/files/CO_417_MANUAL_DESARROLLADOR_0.pdf); [sodapy, cliente de la API de datos abiertos](https://github.com/afeld/sodapy/); [ydata-profiling, reporte automático de EDA](https://docs.profiling.ydata.ai/latest/reference/resources/); [EDA para series de tiempo](https://ydata.ai/resources/how-to-do-an-eda-for-time-series).

**⚠ Sobre el uso de IA:** úsala como lo hace un analista profesional, para pensar, programar, verificar y revisar. Pero **redacta tú**, con tus palabras; **entiende** cada línea de código y cada decisión, y **no copies** respuestas tal cual. **El jurado te va a preguntar** por qué tomaste cada decisión, y en la sustentación no hay IA.

## 4. Qué entregas

1. **Consolidación del documento base (versión final del anteproyecto).** Reescribe y mejora al máximo todos los apartados de tu anteproyecto: problema, justificación, objetivos, marco de referencia y metodología. Ya no es un borrador: es la base formal de tu trabajo de grado. En la metodología declara CRISP-DM e incluye como figura la Ruta del proyecto, adaptada a tu proyecto.
2. **Desarrollo del objetivo específico 1** (Desarrollo del proyecto). Documenta el proceso que seguiste, la evidencia (gráficas, tablas, fragmentos de código) y los hallazgos de tu primer objetivo, y explica cómo sientan las bases del siguiente.
3. **Disponibilidad de datos y código.** Al final del documento, una sección con los enlaces a Colab, GitHub y la fuente de los datos.
4. **Protocolo de evaluación** (una tabla al final de la metodología). Antes de entrenar cualquier modelo, deja escrito cómo vas a evaluar. Así tus resultados del Hito 2 y del Hito 3 se comparan contra reglas fijadas desde el inicio y nadie puede decir que elegiste la métrica que mejor te quedó. 

  | Elemento | Qué defines | Ejemplo |
  | --- | --- | --- |
  | Métrica principal | La métrica con la que elegirás el mejor modelo | F1-macro (clasificación) o RMSE (regresión) |
  | Métricas secundarias | Las que reportarás además de la principal | AUC-PR y MCC, o MAE y MAPE |
  | Partición y validación | Cómo separarás los datos y cuántas veces repetirás la validación | 20 % de prueba y validación cruzada repetida 5×2; si hay fechas, TimeSeriesSplit con al menos 5 cortes |
  | Línea base | El modelo más simple contra el que te compararás | Predecir la clase más frecuente, la media o el valor del periodo anterior |
  | Criterio de éxito | Qué mejora frente a la línea base considerarás relevante | Una mejora práctica acordada previamente, con su incertidumbre y una comparación estadística adecuada |
  | Prueba estadística | Cómo mostrarás que la diferencia entre modelos no es casualidad | Una prueba adecuada al diseño, con sus supuestos y correcciones justificados |

  Si tu enfoque es descriptivo, define en su lugar los KPIs con su fórmula, la referencia con la que los compararás (meta, periodo anterior o grupo de control) y las pruebas de hipótesis que usarás en el Hito 3. Si más adelante necesitas cambiar algo del protocolo, justifícalo en la bitácora de decisiones.
5. **Declaración de uso de IA.** Una sección con la herramienta, para qué la usaste y en qué partes.

## 5. Lista de chequeo técnica (sugerida)

- ☐ **Dataset real:** datos abiertos de Colombia (por ejemplo, datos.gov.co) u otra fuente real. Elige los datos según tu pregunta y acuerda con tu director si un dataset de práctica es adecuado para el alcance de tu investigación.
- ☐ **Adquisición:** por API o con descarga manual, guardando una copia con la fecha de descarga.
- ☐ **Ficha del dataset:** fuente, enlace, licencia o autorización, fecha de descarga, periodo cubierto, número de registros y de variables, y variable objetivo.
- ☐ **Diccionario de datos:** para cada variable, nombre, tipo, unidad, descripción, valores posibles o rango y porcentaje de faltantes.
- ☐ **ETL/ELT en Python:** tipos de dato, duplicados, faltantes (cuántos y cómo se trataron), atípicos y transformaciones, con una tabla de conteos antes y después. Las transformaciones que aprenden de los datos (imputación, escalado, codificación) no se ajustan aquí sobre todo el dataset: se aplicarán dentro de un Pipeline en el Hito 2 para evitar fuga de información.
- ☐ **EDA multivariado:** distribución de la variable objetivo y de las variables principales, correlaciones de Pearson y Spearman, multicolinealidad (VIF), tendencia y estacionalidad si hay fechas, y desbalance de clases si es clasificación.
- ☐ **Protocolo de evaluación:** tabla con métrica principal, métricas secundarias, partición y validación, línea base, criterio de éxito y prueba estadística (o KPIs y referencias, si tu enfoque es descriptivo).
- ☐ **Bitácora de decisiones** como anexo: una tabla con fecha, decisión, alternativas consideradas, por qué la elegiste y evidencia. Llénala a medida que avanzas, no al final.
- ☐ **Código:** Google Colab guardado en un repositorio público de GitHub con la estructura de la guía [Cómo entregar el código](colab-y-github.md) y la versión v0.1. Debe correr de principio a fin sin errores y con semilla fija.
- ☐ **Reglas de reporte:** cada figura y tabla lleva un título que se entienda solo y dos o tres frases de interpretación debajo. Ninguna cifra se escribe a mano: todas salen del código.
- ☐ **Formato:** un único PDF en el formato establecido por tu programa, con [Normas APA](escritura-y-referencias.md) 7.ª edición y los nombres completos de todos los integrantes en la portada. Extensión y soportes según tu programa. Evidencias recomendadas: cuaderno de Colab, repositorio con la versión v0.1 y licencia o autorización de uso de los datos.

## 6. Ideas para profundizar (opcionales)

Elige las ideas que aporten a tu pregunta y acuerda su alcance con tu director. Su utilidad depende del tipo de proyecto y de los datos disponibles.

| Idea | Qué hacer en este hito | Por qué mejora tu trabajo |
| --- | --- | --- |
| **Compara alternativas** | Prueba dos formas de tratar los datos faltantes o los atípicos (por ejemplo, rellenar con la mediana frente a estimar a partir de registros parecidos) y muestra en una tabla cuál altera menos tus datos. | Tu limpieza deja de ser un paso automático y se vuelve una decisión justificada. |
| **Demuestra que se sostiene** | Revisa si los hallazgos del EDA se repiten en distintos periodos o subgrupos de tus datos. | Muestras que tus hallazgos no son casualidad de un corte de los datos. |
| **Suma contexto** | Une a tus datos una segunda fuente real que comparta una llave (lugar, fecha o código) y aporte información nueva. | Más contexto suele explicar mejor la variable objetivo. |
| **Tradúcelo a decisiones** | Cierra el EDA con tres hallazgos escritos en el lenguaje del problema y la decisión que sugiere cada uno. | Conectas el análisis con el problema que quieres resolver. |

[Volver al inicio](../README.md)

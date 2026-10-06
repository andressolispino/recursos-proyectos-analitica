# Hito 3: resultados, discusión y documento final

Estas orientaciones son adaptables; no constituyen una rúbrica ni reemplazan las indicaciones de tu director. Justifica cada técnica y ajusta la cantidad de modelos, las particiones y las variantes al problema.

**Cuidado con la inferencia:** las particiones de validación cruzada repetida comparten datos y no son automáticamente observaciones independientes. Revisa los supuestos antes de aplicar Friedman, Nemenyi, Wilcoxon o bootstrap. Para datos temporales o agrupados, usa una estrategia que preserve esas dependencias. Reporta también el tamaño de la mejora y sus límites.

## 1. Dónde estás en la ruta

En este hito trabajas la **etapa 4** de la [Ruta del proyecto](ruta-del-proyecto.md) (inferencia estadística y pruebas de hipótesis; importancia de variables y SHAP), con técnicas justificadas según el proyecto, y, si corresponde, las **etapas 5 y 6**, que son opcionales.

## 2. Qué vas a lograr

**Propósito.** Completar el último objetivo, demostrar el rigor analítico de los resultados y cerrar el documento. Probar que tus resultados no son casualidad y explicar por qué tu modelo decide lo que decide es lo que convierte tu trabajo en un proyecto sólido y defendible.

**Resultado de aprendizaje.** Interpreta y discute los resultados frente a la pregunta, los objetivos y los referentes; elabora un documento final con rigor académico y trazabilidad; y prepara la sustentación ante jurados.

## 3. Recursos para este hito

- [Plantilla general de documento](../plantillas/documento-de-investigacion.md)
- [Plantilla de presentación de sustentación (.pptx)](../plantillas/presentacion.md) para tus diapositivas finales.
- [Cómo entregar el código (Colab y GitHub)](colab-y-github.md): cómo subir la versión final y crear la versión v1.0 desde la página de GitHub. Incluye, como opción, cómo obtener un DOI con Zenodo. ¿Dudas con GitHub? Esa guía tiene dos videos tutoriales en español y el enlace a la [documentación oficial de GitHub](https://docs.github.com/es/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).
- [Guía de prompts de IA](../prompts/README.md): prompts listos para la prueba estadística, los intervalos de confianza, la interpretación de SHAP, la revisión de tu discusión y el simulacro de sustentación (prompts 16 a 23, incluidos la tabla de ablación y la evaluación de usabilidad SUS), y prompts para revisar cada capítulo del documento final con criterios de jurado: resultados y discusión, conclusiones, introducción y resumen, citas y referencias, repositorio y plan de ajustes (R6 a R13, incluida la autoverificación de buenas prácticas de reporte).
- [Tablas y figuras sugeridas (opcional)](../plantillas/tablas-y-figuras.md): incluye el diagrama de diferencia crítica y los gráficos SHAP.
- [Normas APA](escritura-y-referencias.md) · [Escritura y referencias](escritura-y-referencias.md)
- **Códigos de ayuda por tema**: ejemplos reales en GitHub para cada paso de este hito. 

  | Tema de la ruta | Ejemplos en GitHub (cuadernos de proyectos reales) |
  | --- | --- |
  | **Etapa 4 · Comparación estadística de modelos** | - [Friedman y diagrama de diferencia crítica](https://gist.github.com/milenamonteiro/33ea5223c7cd43cabd71fc96375908c1) (con [explicación paso a paso](https://dev.to/milenamonteiro/comparing-machine-learning-algorithms-using-friedman-test-and-critical-difference-diagrams-in-python-10a9))<br>- [Friedman, Wilcoxon-Holm y diagrama de diferencia crítica](https://github.com/hfawaz/cd-diagram) |
  | **Etapa 4 · Explicabilidad con SHAP** | - [SHAP global y de casos individuales](https://github.com/InfinitePraveen/Churn-Prediction-SHAP/blob/main/notebooks/02_shap_explainability.ipynb)<br>- [Pruebas estadísticas, XGBoost y SHAP](https://github.com/notzenotz/bank-churn-prediction/blob/main/bank_churn_analysis.ipynb)<br>- [Gráficos resumen y de dependencia](https://github.com/tiggachris/churn-xgboost-shap/blob/main/model%20(1).ipynb) |
  | **Etapa 4 · Importancia por permutación (para contrastar con SHAP)** | - [Importancia por permutación con variables correlacionadas](https://github.com/wiherreira/XAI-CounterfactualExplanations/blob/master/project_plot_permutation_importance_multicollinear.ipynb) |
  | **Etapa 4 · Intervalos de confianza de las métricas** | - [Bootstrap para métricas de clasificación](https://github.com/aws-samples/confidence-intervals-for-ml-metrics-tutorials/blob/main/classification-tasks.ipynb)<br>- [Intervalos con bootstrapping](https://github.com/luferrer/ConfidenceIntervals/blob/main/confidence_intervals_with_bootstrapping.ipynb)<br>- [Bootstrap dentro de un proyecto completo](https://github.com/JuancarlosPG2004/Credit-Score-Classification/blob/main/Report_notebook.ipynb) |
  | **Etapa 5 (opcional) · Contrafactuales y equidad** | - [Contrafactuales con DiCE](https://github.com/wiherreira/XAI-CounterfactualExplanations/blob/master/3_DiCE_explainer_on_Adult_Dataset.ipynb)<br>- [Equidad de un modelo de crédito con Fairlearn](https://github.com/gayathrick2007-max/fairloan/blob/main/FairLoan.ipynb)<br>- [Auditorías de sesgo en varios dominios](https://github.com/Yipjunwei/Fair-Code/tree/main/notebooks) |
  | **Etapa 6 (opcional) · Despliegue** | - [Despliegue con Streamlit](https://github.com/JDAG-SUP/mineria-de-datos-jd-y-dm/blob/main/notebooks/03_Despliegue_Streamlit.ipynb) (en español)<br>- [App de pronóstico en Streamlit](https://github.com/AravindLN123/Energy-Demand-Forecasting-SARIMA-LSTM-/blob/main/Code/streamlit_app.py)<br>- [API con FastAPI y modelo calibrado](https://github.com/MarlonPC32/credit-default-decision-service) |

  Son repositorios de otros estudiantes y analistas (la mayoría en inglés). Ábrelos para ver cómo resolvieron cada paso y adapta las ideas a tus datos. Para ejecutar un cuaderno en Colab, cambia `github.com` por `colab.research.google.com/github` en su dirección. Si reutilizas código ajeno, entiéndelo y cítalo en tu documento.
- Todo lo anterior también está en la sección [Catálogo de ejemplos de código](../recursos/ejemplos-de-codigo.md).
- Para profundizar: [autorank: Friedman, Nemenyi y diagrama de diferencia crítica](https://sherbold.github.io/autorank/); [documentación de SHAP](https://shap.readthedocs.io/); [Interpretable Machine Learning, de Christoph Molnar (libro gratuito en línea)](https://christophm.github.io/interpretable-ml-book/); [Kaggle Learn, curso Machine Learning Explainability](https://www.kaggle.com/learn).

**⚠ Sobre el uso de IA:** úsala como lo hace un analista profesional, para calcular, verificar y revisar. Pero **redacta tú** tus resultados, tu discusión y tus conclusiones, con tus palabras; **entiende** cada prueba, cada intervalo y cada interpretación, y **no copies** respuestas tal cual. **El jurado te va a preguntar** por todo lo que escribas, y en la sustentación no hay IA.

## 4. Qué entregas

1. **Último objetivo específico** en la capítulo de desarrollo del proyecto.
2. **Documento completo**, conforme a la plantilla de tu programa: introducción; desarrollo completo de los objetivos específicos y del proyecto; resultados, análisis y discusión sustentados con evidencias; conclusiones y recomendaciones; resumen, abstract y palabras clave; referencias y anexos (incluida la bitácora de decisiones); revisión final de redacción, citación y referencias según APA 7.ª edición.
3. **Diapositivas para la sustentación:** versión final en PDF para 15 minutos, alineada con el documento.
4. **Disponibilidad de datos y código** actualizada (con el enlace al despliegue, si existe, y el DOI de Zenodo, si decides obtenerlo: es opcional) y **Declaración de uso de IA** (sugerida).
5. **Ficha técnica del proyecto (opcional)**: si quieres, agrégala como Anexo A con la [ficha técnica de esta biblioteca](../plantillas/ficha-tecnica.md). Es una página que resume datos, protocolo, mejor resultado, prueba estadística y hallazgo principal, y te sirve de guion para la sustentación.

## 5. Lista de chequeo técnica (sugerida)

- ☐ **Comparación estadística de modelos:** prueba de Friedman con post hoc de Nemenyi y diagrama de diferencia crítica, o Wilcoxon con corrección de Holm, sobre la métrica principal de cada partición de la validación repetida (`results/tables/metricas_por_particion.csv` del Hito 2). Reporta la prueba, el estadístico y el valor p.
- ☐ **Intervalos de confianza del 95 %** para la métrica principal del mejor modelo y de la línea base, por bootstrap sobre el conjunto de prueba o a partir de las particiones repetidas. Así se ve si la mejora es real o cabe dentro de la variación normal.
- ☐ **Tabla de ablación** (enfoque predictivo): parte de tu modelo final y quita una decisión a la vez (por ejemplo, las variables que creaste, el balanceo de clases, la selección de variables o la optimización de hiperparámetros), con el mismo esquema de validación de tu protocolo. Reporta la métrica principal con su intervalo de confianza para cada variante (mínimo 3 variantes además del modelo completo) y guarda la tabla en results/tables/ablacion.csv. Así demuestras qué aporta cada decisión. Apóyate en el prompt 21 de la [guía de prompts](../prompts/README.md).
- ☐ **Si tu enfoque es descriptivo:** en lugar de comparar modelos y aplicar SHAP, aplica pruebas de hipótesis a las diferencias que muestran tus KPIs (entre grupos, periodos o regiones), con intervalos de confianza, y explica qué variables las impulsan.
- ☐ **Si tu enfoque es descriptivo: evaluación de usabilidad del tablero.** Aplica el cuestionario SUS (System Usability Scale, 10 afirmaciones con escala de 1 a 5) a 5 usuarios o más del público al que va dirigido, después de pedirles que resuelvan 2 o 3 tareas con el tablero. Reporta el puntaje promedio (de 0 a 100) con su variabilidad y las mejoras que hiciste a partir de lo observado. Las 10 afirmaciones y el cálculo están en el prompt 22 de la [guía de prompts](../prompts/README.md).
- ☐ **Explicabilidad del mejor modelo con SHAP:** gráfico resumen, importancia, dependencia de las 3 variables principales y 2 o 3 casos individuales, interpretados en el lenguaje del dominio.
- ☐ **Discusión:** qué variables explican el resultado y por qué, comparación con 3 a 5 estudios de tu marco de referencia, limitaciones y amenazas a la validez.
- ☐ **Ficha del modelo final** en models/model_card.md: datos, uso previsto, métricas y límites.
- ☐ **Repositorio final** con la versión v1.0. El README explica cómo regenerar todas las tablas y figuras del documento e incluye el **entorno de cómputo**: versión de Python, librerías y versiones (requirements.txt), tipo de máquina de Colab (CPU o GPU) y tiempo de entrenamiento de cada modelo.
- ☐ **Reglas de reporte:** las mismas de los hitos anteriores; además, todas las cifras del documento coinciden con las tablas de results/tables.
- ☐ **Autoverificación de buenas prácticas de reporte:** revisa tu documento con la [lista de buenas prácticas de reporte](lista-de-reporte.md) (32 puntos, adaptada de un estándar internacional para proyectos con aprendizaje automático) y completa lo que falte. Puedes apoyarte en el prompt R13 de la guía.
- ☐ **Formato:** dos PDF: el documento final en el formato establecido por tu programa, con APA 7 y los nombres completos de todos los integrantes en la portada, y las diapositivas. Extensión y soportes según tu programa. Evidencias recomendadas: cuaderno de Colab, repositorio con la versión v1.0 y, si existe, enlace al despliegue.

## 6. Ideas para profundizar (opcionales)

Elige las ideas que aporten a tu pregunta y acuerda su alcance con tu director. Su utilidad depende del tipo de proyecto y de los datos disponibles.

| Idea | Qué hacer en este hito | Por qué mejora tu trabajo |
| --- | --- | --- |
| **Compara alternativas** | Contrasta la importancia de variables de SHAP con otro método (por ejemplo, importancia por permutación) y comenta en qué coinciden y en qué no. | Tus conclusiones no dependen de una sola técnica. |
| **Demuestra que se sostiene** | Valida el mejor modelo en datos que no usaste para entrenar ni ajustar (por ejemplo, el periodo más reciente o una región distinta) o repite el entrenamiento con varias semillas, y muestra que el resultado se mantiene. | Muestras que tu modelo funciona más allá de los datos con los que lo construiste. |
| **Suma contexto** | Analiza dónde se equivoca más tu modelo (por subgrupo, periodo o región) y propone por qué. | Muestras los límites reales de tu solución. |
| **Tradúcelo a decisiones** | Entrega algo que un usuario pueda usar: un tablero, una aplicación sencilla o una guía de decisiones basada en tus resultados. | Tu proyecto pasa de un análisis a una herramienta. |

**Etapas 5 y 6 de la ruta (opcionales).** Son una forma de aplicar estas ideas: inferencia causal (DoWhy o EconML), análisis contrafactual (DiCE), análisis de sesgos y equidad por grupos (Fairlearn), intervalos de predicción (MAPIE) o despliegue del modelo (Streamlit, Gradio o FastAPI).

[Volver al inicio](../README.md)

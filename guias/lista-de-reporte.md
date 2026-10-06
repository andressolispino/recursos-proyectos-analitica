# Lista de buenas prácticas de reporte: 32 puntos

Antes de entregar el Hito 3, revisa que tu documento responda cada punto de esta lista. Es una adaptación de **REFORMS**, un estándar internacional de buenas prácticas de reporte para proyectos que usan aprendizaje automático, construido por consenso entre investigadores de varias disciplinas. Cumplirla hace que tu trabajo sea claro, verificable y reproducible, y te prepara para las preguntas del jurado.

**Cómo usarla**

1. Para cada punto, busca en tu documento dónde está y márcalo como Sí, Parcial o No.
2. Completa lo que falte antes de entregar. No necesitas adjuntar esta lista.
3. Puedes apoyarte en el prompt **R13** de la guía de prompts, que revisa tu documento contra estos 32 puntos y cita tu texto como evidencia.
4. **Si tu enfoque es descriptivo**, responde los bloques 1 a 4 y 8; en los bloques 5 a 7, aplica lo que corresponda a tus KPI y a tus pruebas de hipótesis.

| Punto | Tu documento debe dejar claro… | Dónde suele ir | ¿Cumple? |
| --- | --- | --- | --- |
| **1. Objetivo del estudio** |  |  |  |
| **1a** | A qué población, periodo o contexto se refieren tus conclusiones. | Planteamiento y metodología | ☐ Sí ☐ Parcial ☐ No |
| **1b** | Por qué elegiste esa población o ese contexto. | Justificación | ☐ Sí ☐ Parcial ☐ No |
| **1c** | Por qué el aprendizaje automático es adecuado para tu pregunta, frente a métodos más simples. | Justificación y metodología | ☐ Sí ☐ Parcial ☐ No |
| **2. Reproducibilidad computacional** |  |  |  |
| **2a** | El conjunto de datos usado, con su enlace (y DOI, si lo tiene) y la fecha de descarga. | Disponibilidad de datos y código | ☐ Sí ☐ Parcial ☐ No |
| **2b** | El código que entrena, evalúa y produce los resultados: enlace al repositorio y a la versión v1.0. | Disponibilidad de datos y código | ☐ Sí ☐ Parcial ☐ No |
| **2c** | El entorno de cómputo: Colab o equipo local, CPU o GPU, versión de Python y de las librerías. | README y metodología | ☐ Sí ☐ Parcial ☐ No |
| **2d** | Un README con las instrucciones para regenerar los resultados. | Repositorio | ☐ Sí ☐ Parcial ☐ No |
| **2e** | Un cuaderno o script que produce todas las tablas y figuras del documento. | Repositorio | ☐ Sí ☐ Parcial ☐ No |
| **3. Calidad de los datos** |  |  |  |
| **3a** | Las fuentes de datos, por separado si el entrenamiento y la evaluación vienen de fuentes distintas. | Metodología | ☐ Sí ☐ Parcial ☐ No |
| **3b** | De dónde proviene la muestra: cobertura, periodo y criterios de la fuente. | Metodología | ☐ Sí ☐ Parcial ☐ No |
| **3c** | Por qué esos datos sirven para la tarea de modelado. | Metodología | ☐ Sí ☐ Parcial ☐ No |
| **3d** | La variable objetivo, con su definición y sus estadísticos descriptivos. | Desarrollo (EDA) | ☐ Sí ☐ Parcial ☐ No |
| **3e** | El tamaño de la muestra y la frecuencia de cada clase (o el rango de la variable objetivo). | Desarrollo (EDA) | ☐ Sí ☐ Parcial ☐ No |
| **3f** | El porcentaje de datos faltantes, por clase si es clasificación. | Desarrollo (EDA) | ☐ Sí ☐ Parcial ☐ No |
| **3g** | Por qué los datos representan a la población de 1a, o qué sesgos podrían tener. | Metodología y limitaciones | ☐ Sí ☐ Parcial ☐ No |
| **4. Preparación de los datos** |  |  |  |
| **4a** | Si excluiste registros: cuántos y por qué. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **4b** | Cómo trataste los registros imposibles o corruptos. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **4c** | Todas las transformaciones, desde los datos crudos hasta los datos de modelado. | Desarrollo y bitácora de decisiones | ☐ Sí ☐ Parcial ☐ No |
| **5. Modelado** |  |  |  |
| **5a** | La descripción de todos los modelos entrenados, no solo del mejor. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **5b** | Por qué elegiste esos tipos de modelo. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **5c** | Cómo evaluaste: partición y validación, según tu protocolo. | Metodología (protocolo de evaluación) | ☐ Sí ☐ Parcial ☐ No |
| **5d** | Cómo seleccionaste el modelo final. | Resultados | ☐ Sí ☐ Parcial ☐ No |
| **5e** | Cómo ajustaste los hiperparámetros del modelo final: espacio de búsqueda, método y número de ensayos. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **5f** | Por qué tus comparaciones son contra líneas base adecuadas. | Resultados | ☐ Sí ☐ Parcial ☐ No |
| **6. Fuga de información** |  |  |  |
| **6a** | Que la preparación y el modelado usan solo datos de entrenamiento en cada partición (por ejemplo, con un Pipeline). | Metodología y desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **6b** | Cómo manejaste duplicados o dependencias entre entrenamiento y prueba (misma entidad, mismo periodo). | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **6c** | Que cada variable usada es legítima: se conoce en el momento en que se haría la predicción. | Desarrollo | ☐ Sí ☐ Parcial ☐ No |
| **7. Métricas e incertidumbre** |  |  |  |
| **7a** | Todas las métricas usadas para evaluar y comparar modelos. | Resultados | ☐ Sí ☐ Parcial ☐ No |
| **7b** | La incertidumbre de las métricas (intervalos de confianza del 95 %) y cómo la calculaste. | Resultados | ☐ Sí ☐ Parcial ☐ No |
| **7c** | Por qué elegiste la prueba estadística y cómo verificaste sus supuestos. | Resultados | ☐ Sí ☐ Parcial ☐ No |
| **8. Generalización y limitaciones** |  |  |  |
| **8a** | La evidencia de que tus resultados se sostienen fuera de los datos de entrenamiento, y sus limitaciones. | Discusión | ☐ Sí ☐ Parcial ☐ No |
| **8b** | Los contextos en los que no esperas que tus resultados se cumplan. | Discusión y conclusiones | ☐ Sí ☐ Parcial ☐ No |

Fuente: adaptado al español y al contexto de esta biblioteca a partir de Kapoor et al. (2024), *REFORMS: Consensus-based recommendations for machine-learning-based science*, [https://doi.org/10.1126/sciadv.adk3452](https://doi.org/10.1126/sciadv.adk3452). Sitio del estándar: [reforms.cs.princeton.edu](https://reforms.cs.princeton.edu/).

[Volver al inicio](../README.md)

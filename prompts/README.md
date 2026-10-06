# Prompts para proyectos y tesis de analítica de datos

36 prompts completos: **23 para el trabajo analítico** y **13 para revisar el documento**. Son herramientas de apoyo para decidir, programar, verificar y revisar. La redacción, las decisiones y la defensa corresponden al estudiante.

## Cómo usarlos

1. Completa el [bloque de contexto](contexto-del-proyecto.txt), incluidos tu nivel académico y el alcance acordado con tu director.
2. Abre el prompt que necesitas y copia completo su bloque de texto.
3. Sustituye el bloque de contexto por el tuyo, completa los corchetes y deja en los insumos solo lo que realmente adjuntas.
4. Adjunta evidencia revisada: estructura de los datos, tablas, figuras, código o tu capítulo.
5. Comprueba los resultados, las referencias y los avisos de información faltante.
6. Lleva las decisiones a tu bitácora y redacta con tus palabras.

**Uso responsable:** no adjuntes datos personales ni información confidencial. Declara qué herramienta utilizaste, para qué y qué verificaste. Si no puedes explicar una línea de código, una métrica o una decisión, revísala antes de usarla.

Los criterios de los prompts son adaptables. Define con tu director cuáles aplican a tu investigación; no todas las técnicas son necesarias para todos los proyectos.

## Prepara los insumos

- [Cuaderno de Colab para generar un resumen de estructura](../notebooks/00_insumos_ia.ipynb).
- [Código descargable](../codigo/generar_insumos_ia.py): genera tipos, faltantes y conteos sin incluir filas ni valores de las columnas.
- [Ficha y diccionario de datos](../plantillas/diccionario-de-datos.csv).
- [Protocolo de evaluación](../plantillas/protocolo-de-evaluacion.md).
- Figuras, resultados por partición, mensaje de error completo o el capítulo que quieres revisar, según el prompt.

El resumen de estructura también puede revelar información del proyecto. Revísalo antes de compartirlo y excluye columnas o nombres confidenciales.

## Prompts de trabajo

| Código | Tarea |
| --- | --- |
| P1 | [1. Afinar el problema, la pregunta y los objetivos](P1.md) |
| P2 | [2. Evaluar si el conjunto de datos sirve](P2.md) |
| P3 | [3. Descargar datos de datos.gov.co por API](P3.md) |
| P4 | [4. Construir el diccionario de datos](P4.md) |
| P5 | [5. Plan de limpieza (ETL) con decisiones justificadas](P5.md) |
| P6 | [6. Diseñar el EDA univariado, bivariado y multivariado](P6.md) |
| P7 | [7. Contrastar tu interpretación de una figura o tabla](P7.md) |
| P8 | [8. Fijar el protocolo de evaluación](P8.md) |
| P9 | [9. Proponer ingeniería de características](P9.md) |
| P10 | [10. Auditar tu código contra la fuga de información](P10.md) |
| P11 | [11. Programar la batería de modelos con validación repetida](P11.md) |
| P12 | [12. Optimizar hiperparámetros con Optuna](P12.md) |
| P13 | [13. Resolver un error de código](P13.md) |
| P14 | [14. Interpretar los resultados de la batería](P14.md) |
| P15 | [15. Enfoque descriptivo: modelo dimensional y KPI](P15.md) |
| P16 | [16. Elegir y correr la prueba estadística](P16.md) |
| P17 | [17. Calcular intervalos de confianza del 95 %](P17.md) |
| P18 | [18. Explicar SHAP en el lenguaje del problema](P18.md) |
| P19 | [19. Poner a prueba tu discusión como lo haría un jurado](P19.md) |
| P20 | [20. Revisar la coherencia de las cifras en todo el documento](P20.md) |
| P21 | [21. Construir la tabla de ablación](P21.md) |
| P22 | [22. Enfoque descriptivo: evaluar la usabilidad del tablero (SUS)](P22.md) |
| P23 | [23. Simulacro de preguntas de los jurados](P23.md) |

## Prompts para revisar tu documento

| Código | Revisión |
| --- | --- |
| R1 | [R1. Revisar el planteamiento del problema y la pregunta](R1.md) |
| R2 | [R2. Revisar la justificación](R2.md) |
| R3 | [R3. Revisar los objetivos](R3.md) |
| R4 | [R4. Revisar el marco de referencia](R4.md) |
| R5 | [R5. Revisar la metodología y el protocolo de evaluación](R5.md) |
| R6 | [R6. Revisar el desarrollo de un objetivo específico](R6.md) |
| R7 | [R7. Revisar resultados, análisis y discusión](R7.md) |
| R8 | [R8. Revisar conclusiones y recomendaciones](R8.md) |
| R9 | [R9. Revisar introducción, resumen, abstract y palabras clave](R9.md) |
| R10 | [R10. Revisar citas y referencias APA 7, tablas, figuras y redacción](R10.md) |
| R11 | [R11. Revisar el repositorio, el README y Disponibilidad de datos y código](R11.md) |
| R12 | [R12. Convertir la retroalimentación del docente en un plan de ajustes](R12.md) |
| R13 | [R13. Autoverificación con la lista de buenas prácticas de reporte](R13.md) |

[Volver al inicio](../README.md)

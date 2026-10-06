# Protocolo de evaluación

Completa antes de seleccionar modelos o interpretar resultados. Si cambias una decisión, documenta cuándo, por qué y qué datos ya habías observado.

| Elemento | Decisión de mi proyecto | Justificación |
| --- | --- | --- |
| Unidad de análisis y población | [completar] | [completar] |
| Objetivo, tarea y momento de predicción | [completar] | [completar] |
| Métrica principal o KPI | [definición y fórmula] | [relación con la decisión] |
| Métricas secundarias | [completar] | [completar] |
| Partición de prueba | [temporal, por grupos o estratificada; periodo y tamaño] | [cómo evita contaminación] |
| Validación para ajustar modelos | [esquema, repeticiones y semilla] | [por qué representa el uso real] |
| Preprocesamiento | [pipeline y ajuste solo en entrenamiento] | [cómo evita fuga] |
| Línea base o referencia | [modelo simple, meta o periodo anterior] | [comparador pertinente] |
| Criterio de éxito | [mejora práctica acordada] | [valor para el usuario] |
| Incertidumbre | [método y unidad de remuestreo] | [supuestos y dependencias] |
| Comparación estadística si aplica | [prueba, hipótesis y corrección] | [supuestos comprobables] |
| Presupuesto de búsqueda | [tiempo, espacio y número de ensayos] | [comparación justa] |
| Condiciones de uso y límites | [completar] | [completar] |

Para inteligencia de negocios, agrega fórmula de cada KPI, totales de control, referencia de comparación y evaluación de utilidad o usabilidad del tablero.

Evita ajustar decisiones con el conjunto de prueba. Las particiones de validación cruzada repetida comparten datos: revisa la dependencia antes de tratarlas como observaciones independientes en una prueba.

[Volver al inicio](../README.md)

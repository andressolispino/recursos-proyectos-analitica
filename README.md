# Recursos para proyectos y tesis de analítica de datos

Biblioteca de apoyo para estudiantes de especialización y maestría en analítica y ciencia de datos. Reúne una ruta de trabajo, guías metodológicas, prompts, plantillas, código probado y proyectos reales de ejemplo para avanzar desde la pregunta de investigación hasta la sustentación.

**Mantenida por Andrés Felipe Solís Pino.** Los recursos se adaptan al contexto de cada proyecto y complementan las orientaciones de su director y las reglas de su programa.

## Empieza aquí

1. Ubica tu proyecto en la [ruta metodológica](guias/ruta-del-proyecto.md) (seis etapas basadas en CRISP-DM).
2. Define tu [protocolo de evaluación](plantillas/protocolo-de-evaluacion.md) antes de modelar.
3. Abre la guía del hito en el que estás y usa los recursos que respondan a tu pregunta.
4. Lleva tus decisiones a la [bitácora](plantillas/bitacora-de-decisiones.csv) y conserva la trazabilidad entre código, tablas, figuras y documento.

## Encuentra lo que necesitas

| Quiero… | Recurso |
| --- | --- |
| Organizar la investigación | [Ruta del proyecto](guias/ruta-del-proyecto.md) |
| Formular el problema y preparar los datos | [Hito 1: datos, ETL y EDA](guias/hito-1-datos-y-preparacion.md) |
| Construir y comparar modelos o un tablero | [Hito 2: desarrollo y modelado](guias/hito-2-modelado.md) |
| Interpretar resultados y cerrar el documento | [Hito 3: resultados y discusión](guias/hito-3-resultados-y-discusion.md) |
| Usar IA con contexto y evidencia | [23 prompts de trabajo y 13 de revisión](prompts/README.md) |
| Ver proyectos reales completos, cuaderno por cuaderno | [Proyectos de ejemplo](proyectos-ejemplo/README.md) |
| Hacer la prueba estadística, los intervalos de confianza, la ablación y SHAP | [Código de apoyo](codigo/README.md) · [Cuaderno de flujo completo](notebooks/01_flujo_rigor_analitico.ipynb) |
| Ver ejemplos de código de otros autores por tema | [Catálogo de cuadernos y proyectos](recursos/ejemplos-de-codigo.md) |
| Organizar Colab y GitHub | [Guía de código, versiones y reproducción](guias/colab-y-github.md) |
| Redactar y citar | [Escritura y referencias](guias/escritura-y-referencias.md) |
| Revisar la calidad del informe | [Lista de 32 buenas prácticas de reporte](guias/lista-de-reporte.md) |
| Preparar la sustentación | [Guion de presentación](plantillas/presentacion.md) · [Simulacro de jurado](prompts/P23.md) |

## Plantillas para usar en tu proyecto

- [Estructura del documento de investigación](plantillas/documento-de-investigacion.md).
- [Ficha técnica de una página](plantillas/ficha-tecnica.md).
- [Protocolo de evaluación](plantillas/protocolo-de-evaluacion.md).
- [Diccionario de datos en CSV](plantillas/diccionario-de-datos.csv).
- [Bitácora de decisiones en CSV](plantillas/bitacora-de-decisiones.csv).
- [Registro de experimentos en CSV](plantillas/registro-de-experimentos.csv).
- [README del proyecto](plantillas/readme-del-proyecto.md).
- [Ficha del modelo](plantillas/ficha-del-modelo.md).
- [Tablas y figuras sugeridas](plantillas/tablas-y-figuras.md).

Abre un archivo para consultarlo. Para guardar tu propia copia, usa **Code → Download ZIP** o descarga el archivo que necesites. Los CSV se pueden abrir en una hoja de cálculo y las plantillas de texto se pueden copiar a tu editor.

## Código, cuadernos y proyectos de ejemplo

- **[Código de apoyo](codigo/README.md):** funciones probadas para la batería de modelos con validación repetida, la comparación estadística (Friedman, Nemenyi con diagrama de diferencia crítica y Wilcoxon-Holm), los intervalos de confianza (bootstrap y corregidos), la tabla de ablación, SHAP contra importancia por permutación, el puntaje SUS y la validación de totales de un tablero.
- **[Cuaderno de flujo completo](notebooks/01_flujo_rigor_analitico.ipynb):** usa todo ese código de punta a punta, con los resultados visibles.
- **[Cuaderno de insumos para IA](notebooks/00_insumos_ia.ipynb):** genera un resumen de la estructura de tus datos sin incluir filas ni valores (también como [script](codigo/generar_insumos_ia.py)). Revisa siempre el resultado antes de compartirlo.
- **[Proyectos de ejemplo](proyectos-ejemplo/README.md):** dos trabajos de grado reales y anonimizados, con todos sus cuadernos: pronóstico de la demanda de energía eléctrica (regresión y series de tiempo) y pronóstico de los activos de fondos de inversión colectiva (un cuaderno por modelo, de SARIMA a LSTM).

Para abrir cualquier cuaderno en Colab, cambia `github.com` por `colab.research.google.com/github` en su dirección.

## Estructura del repositorio

```text
├── guias/              ruta del proyecto, guías por hito, Colab y GitHub, escritura, lista de reporte
├── prompts/            36 prompts (P1–P23 de trabajo, R1–R13 de revisión) y bloque de contexto
├── plantillas/         documento, ficha técnica, protocolo, diccionario, bitácora, experimentos, presentación
├── codigo/             código de apoyo en Python, probado
├── notebooks/          cuadernos de Colab listos para usar
├── proyectos-ejemplo/  proyectos reales completos y anonimizados
└── recursos/           catálogo de ejemplos externos y documentación
```

## Si tu programa trabaja por entregas

Ubica cada entrega de tu curso o de tu tesis en el hito que le corresponde. Las fechas, los pesos y las rúbricas los define tu programa; aquí encuentras los recursos técnicos.

## Criterio de uso

Adapta cada técnica a tu pregunta, a los datos y al nivel académico. La IA ayuda a revisar y contrastar; tú redactas, verificas, entiendes el código y respondes por las decisiones. Usa el formato y las reglas de tu programa.

## Licencia y créditos

Los textos, guías, prompts y plantillas de esta biblioteca se publican bajo [CC BY 4.0](LICENSE) y el código de apoyo bajo [licencia MIT](LICENSE-CODE): puedes usarlos y adaptarlos citando la fuente ([cómo citar](CITATION.cff)). Los proyectos de ejemplo se comparten con autorización de sus autores, con fines educativos. Consulta los [créditos y condiciones de uso](CREDITOS.md) y la [documentación complementaria](recursos/documentacion.md). Los enlaces externos mantienen la autoría de sus fuentes y pueden cambiar o solicitar acceso.

La biblioteca es pública para lectura y descarga. El repositorio original lo administra su propietario; consultarlo o descargarlo no concede permiso para modificarlo.

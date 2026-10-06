# Código de apoyo

Funciones en Python, listas para usar en Colab o en tu equipo, que resuelven los requisitos técnicos más exigentes de la [ruta del proyecto](../guias/ruta-del-proyecto.md). Cada archivo trae su explicación al inicio y un ejemplo al final que puedes ejecutar tal cual (`python archivo.py`).

| Archivo | Qué resuelve | Etapa | Genera |
| --- | --- | --- | --- |
| [generar_insumos_ia.py](generar_insumos_ia.py) | Resumen de la estructura de tus datos para usar los [prompts](../prompts/README.md), sin filas ni valores | Todas | `insumos_ia.txt` |
| [bateria_modelos.py](bateria_modelos.py) | Batería de modelos con validación cruzada repetida (o temporal) y registro de experimentos | 3 | `metricas_por_particion.csv`, `resumen_modelos.csv`, `experiments.csv` |
| [comparacion_estadistica.py](comparacion_estadistica.py) | Friedman, Nemenyi con diagrama de diferencia crítica y Wilcoxon con corrección de Holm | 4 | Diagrama en PNG y SVG, tabla por pares |
| [intervalos_confianza.py](intervalos_confianza.py) | IC del 95 % por bootstrap (también por bloques para series de tiempo), IC de la mejora frente a la línea base e IC corregido sobre particiones | 4 | Valores para tus tablas |
| [ablacion.py](ablacion.py) | Tabla de ablación: qué aporta cada decisión del modelo final | 4 | `ablacion.csv` |
| [explicabilidad.py](explicabilidad.py) | SHAP (resumen, importancia, dependencia y casos) contrastado con la importancia por permutación | 4 | Figuras SHAP, `importancia_shap.csv`, `importancia_permutacion.csv` |
| [sus.py](sus.py) | Puntaje SUS de usabilidad de un tablero (enfoque descriptivo) | 4 | Puntajes, media e IC |
| [validacion_totales.py](validacion_totales.py) | Conciliación de registros y totales entre la fuente y tu modelo o tablero (enfoque descriptivo) | 3 | `validacion_totales_<nombre>.csv` |

Las rutas de salida siguen la estructura de carpetas de la [guía de Colab y GitHub](../guias/colab-y-github.md): `results/tables/` y `results/figures/`.

## Míralo funcionando

El cuaderno [01_flujo_rigor_analitico.ipynb](../notebooks/01_flujo_rigor_analitico.ipynb) usa todo este código de punta a punta, con sus resultados ya visibles: batería de siete modelos, prueba de Friedman y diagrama de diferencia crítica, intervalos de confianza, ablación y SHAP.

## Cómo usarlo en Colab

```python
# 1. Descarga el repositorio (una sola vez por sesión)
!git clone -q https://github.com/andressolispino/recursos-proyectos-analitica.git
import sys
sys.path.insert(0, "recursos-proyectos-analitica/codigo")

# 2. Importa lo que necesites
from bateria_modelos import esquema_validacion, evaluar_bateria, tabla_media_de
from comparacion_estadistica import matriz_desempeno, friedman, nemenyi, diagrama_diferencia_critica
from intervalos_confianza import ic_bootstrap, ic_diferencia_bootstrap, formato_ic
```

Dependencias: pandas, NumPy, SciPy, scikit-learn, Matplotlib y SHAP, que normalmente ya vienen en Colab (si falta SHAP, ejecuta `!pip install shap`). Para tu equipo, [requirements.txt](requirements.txt).

## Antes de usarlo en tu proyecto

- **Entiende cada función** antes de usarla: el jurado te preguntará por qué elegiste esa prueba y cómo se calcula el intervalo. Cada archivo explica el método y trae la referencia para citarlo.
- **Las particiones de una validación repetida no son independientes.** Por eso `intervalos_confianza.ic_particiones` aplica por defecto la corrección de Nadeau y Bengio, y las pruebas de Friedman y Wilcoxon deben leerse como apoyo, junto con los intervalos de confianza.
- **Series de tiempo:** usa `esquema_validacion(temporal=True)` (validación con `TimeSeriesSplit`) y `ic_bootstrap(..., bloque=...)` con un bloque acorde a la frecuencia de tus datos (por ejemplo, 24 para datos horarios o 7 para diarios).
- **Fija la semilla** (todas las funciones usan 42 por defecto) para que cualquier tabla o figura se regenere igual.

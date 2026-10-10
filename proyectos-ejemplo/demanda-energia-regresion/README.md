# Pronóstico de la demanda eléctrica del mercado de comercialización del Valle del Cauca (2020–2025)

Trabajo de grado de posgrado en analítica de datos (enfoque predictivo, regresión sobre una serie horaria). Compartido con autorización de sus autores; se retiraron los nombres y los datos personales.

**Pregunta de fondo:** ¿qué tan bien se puede pronosticar la demanda horaria de energía del mercado de comercialización combinando variables del mercado eléctrico, clima, economía y calendario?

## Orden de los cuadernos

| # | Cuaderno | Qué hace | Etapa de la [ruta](../../guias/ruta-del-proyecto.md) |
| --- | --- | --- | --- |
| 0 | [00_consolidacion_dataset.ipynb](00_consolidacion_dataset.ipynb) | Descarga y une las fuentes: clima horario de la API NASA POWER, precio de bolsa y demanda de la API SiMEM de XM (`pydataxm`), TRM desde datos.gov.co (`sodapy`), y archivos cargados a mano (pronóstico y demanda real, IPC e IPP, capacidad solar y térmica, suscriptores SUI-SSPD). Cada fuente sigue los mismos pasos: consultar, extraer, manipular, explorar y recortar el periodo de análisis. | 1 y 2 |
| 1 | [01_exploracion_dataset.ipynb](01_exploracion_dataset.ipynb) | EDA, análisis diagnóstico y preparación de un conjunto de datos por familia de modelos (SARIMAX, regresión robusta, SVM con escalado, Random Forest, redes recurrentes). | 2 |
| 2 | [02_modelos_regresion_analisis.ipynb](02_modelos_regresion_analisis.ipynb) | Versión base de la batería de modelos: pruebas ADF y KPSS, ARIMA, SARIMA, ARIMAX y SARIMAX; luego regresión lineal con selección *forward* y *backward*, SVR, Random Forest, XGBoost y LightGBM. Agrupa el «tipo de día» con *clustering*. | 3 |
| 2.1 | [02_1_modelos_regresion_80_20.ipynb](02_1_modelos_regresion_80_20.ipynb) | La batería completa con partición temporal 80/20 sobre el conjunto depurado, incluido el árbol de decisión. | 3 |
| 2.2 | [02_2_modelos_regresion_dataset_completo_80_20.ipynb](02_2_modelos_regresion_dataset_completo_80_20.ipynb) | Variante sobre el conjunto completo (80/20): usa el tipo de día directamente como variables binarias, sin el agrupamiento por *k-means*. | 3 |
| 2.3 | [02_3_ajuste_hiperparametros_80_20.ipynb](02_3_ajuste_hiperparametros_80_20.ipynb) | Ajuste de hiperparámetros con `GridSearchCV` y validación temporal (`TimeSeriesSplit`). | 3 |
| 2.4 | [02_4_modelos_regresion_90_10.ipynb](02_4_modelos_regresion_90_10.ipynb) | La batería con partición 90/10 y transformaciones cíclicas de las variables de calendario (hora, día de la semana, mes y día del año), para comparar el efecto de la partición. | 3 |

## Datos

Los datos no están en este repositorio. El cuaderno 0 los reconstruye desde sus fuentes públicas:

- **XM – SiMEM** (precio de bolsa, demanda): librería [`pydataxm`](https://pypi.org/project/pydataxm/).
- **NASA POWER** (variables climáticas horarias): [power.larc.nasa.gov](https://power.larc.nasa.gov/).
- **datos.gov.co** (TRM): cliente [`sodapy`](https://github.com/afeld/sodapy).
- **Archivos descargados a mano** (pronóstico y demanda real, IPC e IPP, capacidad instalada, suscriptores SUI-SSPD): el cuaderno indica qué archivo espera en cada sección.

Las rutas apuntan a una carpeta de Google Drive (`/content/drive/MyDrive/ProyectoEspecializacion/...`). Cámbialas por las tuyas antes de ejecutar.

## Qué mirar con ojo crítico

- **Validación:** compara la partición única de los cuadernos 2, 2.1, 2.2 y 2.4 con la validación temporal del 2.3. ¿Cuál da una estimación más confiable del error? Revisa la [lista de chequeo del Hito 2](../../guias/hito-2-modelado.md).
- **Fuga de información:** verifica en qué punto se ajustan el escalado y la selección de variables, y si las variables exógenas estarían disponibles en el momento de pronosticar.
- **Línea base e incertidumbre:** busca contra qué modelo simple se comparan los resultados y si las métricas vienen con intervalos de confianza. Puedes completarlo con el [código de apoyo](../../codigo/README.md).

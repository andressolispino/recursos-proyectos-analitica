"""Intervalos de confianza del 95 % para las métricas de un modelo.

Dos caminos, según lo que tengas:

1. Sobre el conjunto de prueba, por bootstrap: `ic_bootstrap(y_true, y_pred, metrica)`.
   Para series de tiempo usa `bloque=` (bootstrap por bloques) para respetar la dependencia temporal.
2. A partir de las particiones de la validación repetida: `ic_particiones(valores, n_train, n_test)`,
   con la corrección de Nadeau y Bengio (2003) para particiones que comparten datos.

Y para saber si la mejora frente a la línea base es real: `ic_diferencia_bootstrap(...)`, un
bootstrap pareado de la diferencia entre dos modelos sobre el mismo conjunto de prueba.

Referencias:
- Efron, B., & Tibshirani, R. (1993). An introduction to the bootstrap. Chapman & Hall.
- Nadeau, C., & Bengio, Y. (2003). Inference for the generalization error. Machine Learning, 52, 239–281.
"""
from __future__ import annotations

import numpy as np
from scipy import stats

SEMILLA = 42


def _indices_bootstrap(n, rng, bloque=None):
    """Índices de una muestra bootstrap; con `bloque` usa bootstrap circular por bloques."""
    if not bloque or bloque <= 1:
        return rng.integers(0, n, n)
    inicios = rng.integers(0, n, int(np.ceil(n / bloque)))
    return (inicios[:, None] + np.arange(bloque)[None, :]).ravel()[:n] % n


def ic_bootstrap(y_true, y_pred, metrica, n_boot=2000, alpha=0.05, semilla=SEMILLA, bloque=None):
    """IC percentil por bootstrap para `metrica(y_true, y_pred)` sobre el conjunto de prueba.

    metrica: función de sklearn.metrics, p. ej. f1_score con average="macro" (usa functools.partial)
             o mean_absolute_error. Para AUC pasa las probabilidades como y_pred.
    bloque: tamaño de bloque para series de tiempo (p. ej. 24 para datos horarios, 7 para diarios).
    Devuelve un diccionario con el valor puntual, los límites y las réplicas.
    """
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    rng = np.random.default_rng(semilla)
    n = len(y_true)
    replicas = []
    for _ in range(n_boot):
        idx = _indices_bootstrap(n, rng, bloque)
        try:
            replicas.append(metrica(y_true[idx], y_pred[idx]))
        except ValueError:      # p. ej. una réplica con una sola clase para el AUC
            continue
    replicas = np.asarray(replicas)
    bajo, alto = np.percentile(replicas, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return {"valor": float(metrica(y_true, y_pred)), "ic_inferior": float(bajo), "ic_superior": float(alto),
            "nivel": 1 - alpha, "n_boot_validas": len(replicas), "replicas": replicas}


def ic_diferencia_bootstrap(y_true, pred_a, pred_b, metrica, n_boot=2000, alpha=0.05,
                            semilla=SEMILLA, bloque=None):
    """IC de metrica(A) − metrica(B) con bootstrap pareado (mismas filas para ambos modelos).

    Si el intervalo no incluye 0, la diferencia entre A y B no se explica solo por el azar del muestreo.
    """
    y_true, pred_a, pred_b = map(np.asarray, (y_true, pred_a, pred_b))
    rng = np.random.default_rng(semilla)
    n = len(y_true)
    difs = []
    for _ in range(n_boot):
        idx = _indices_bootstrap(n, rng, bloque)
        try:
            difs.append(metrica(y_true[idx], pred_a[idx]) - metrica(y_true[idx], pred_b[idx]))
        except ValueError:
            continue
    difs = np.asarray(difs)
    bajo, alto = np.percentile(difs, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return {"diferencia": float(metrica(y_true, pred_a) - metrica(y_true, pred_b)),
            "ic_inferior": float(bajo), "ic_superior": float(alto), "incluye_cero": bool(bajo <= 0 <= alto)}


def ic_particiones(valores, n_train=None, n_test=None, alpha=0.05, corregido=True):
    """IC t de Student para la media de una métrica sobre las particiones de la validación.

    Con `corregido=True` y los tamaños de entrenamiento y prueba de cada partición aplica la
    corrección de Nadeau y Bengio: var × (1/J + n_test/n_train), que evita intervalos demasiado
    estrechos cuando las particiones comparten datos. Sin tamaños, usa el IC t clásico.
    """
    v = np.asarray(valores, dtype=float)
    J = len(v)
    media, var = v.mean(), v.var(ddof=1)
    if corregido and n_train and n_test:
        se = np.sqrt(var * (1.0 / J + n_test / n_train))
        metodo = "t corregido (Nadeau y Bengio, 2003)"
    else:
        se = np.sqrt(var / J)
        metodo = "t clásico"
    t = stats.t.ppf(1 - alpha / 2, J - 1)
    return {"media": float(media), "ic_inferior": float(media - t * se), "ic_superior": float(media + t * se),
            "nivel": 1 - alpha, "particiones": J, "metodo": metodo}


def formato_ic(res, decimales=3):
    """'0.912 [0.887; 0.934]' para tablas del documento."""
    centro = res.get("valor", res.get("media", res.get("diferencia")))
    return f"{centro:.{decimales}f} [{res['ic_inferior']:.{decimales}f}; {res['ic_superior']:.{decimales}f}]"


if __name__ == "__main__":
    from functools import partial

    from sklearn.metrics import f1_score, mean_absolute_error

    rng = np.random.default_rng(0)
    y = rng.integers(0, 2, 300)
    pred_bueno = np.where(rng.random(300) < 0.9, y, 1 - y)
    pred_base = np.zeros(300, dtype=int)
    f1 = partial(f1_score, average="macro")
    print("F1 modelo:", formato_ic(ic_bootstrap(y, pred_bueno, f1)))
    print("Diferencia vs línea base:", formato_ic(ic_diferencia_bootstrap(y, pred_bueno, pred_base, f1)))
    serie = np.sin(np.arange(500) / 10) + rng.normal(0, 0.1, 500)
    print("MAE con bloques de 24:", formato_ic(ic_bootstrap(serie, serie + rng.normal(0, 0.2, 500),
                                                            mean_absolute_error, bloque=24)))
    print("Particiones:", ic_particiones([0.91, 0.93, 0.90, 0.92, 0.94, 0.91, 0.92, 0.93, 0.90, 0.92],
                                         n_train=455, n_test=114))

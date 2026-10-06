# Organiza y comparte tu código con Colab y GitHub

**No necesitas instalar nada ni escribir comandos:** todo se puede hacer desde la página de GitHub en el navegador. Si prefieres trabajar con una carpeta en tu computador, al final está la opción con el programa GitHub Desktop.

**Para qué sirve.** Google Colab es donde desarrollas y ejecutas tu proyecto; GitHub es donde queda una copia ordenada y con versiones de tu trabajo. Así el docente y los jurados pueden ver de dónde sale cada resultado, y tú puedes volver a cualquier entrega si algo se daña. Es una práctica que mejora tu trabajo y que se usa en cualquier equipo profesional de datos.

GitHub está en inglés: los botones aparecen en **negrita** con su nombre original.

**¿Primera vez en GitHub? Mira primero estos tutoriales en español**

- Video: 

  [Cómo subir archivos a GitHub: añadir archivos y carpetas a un repositorio](https://www.youtube.com/watch?v=VTA67eomfkM)

   (canal Tutorly). Muestra lo mismo que el paso C de esta guía.
- Video corto: 

  [Cómo subir archivos a un repositorio de GitHub, tutorial rápido](https://www.youtube.com/watch?v=CXfch-s-Kag)

   (canal Tu Gurú de Apps).
- Documentación oficial: [Agregar un archivo a un repositorio](https://docs.github.com/es/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) (GitHub Docs, en español).
- Para las versiones v0.1, v0.2 y v1.0: [Administrar versiones (releases) en un repositorio](https://docs.github.com/es/repositories/releasing-projects-on-github/managing-releases-in-a-repository) (GitHub Docs, en español).

## A. Una sola vez: crea el repositorio (5 minutos)

1. Crea una cuenta gratuita en [github.com](https://github.com). Basta con la cuenta de un integrante; los demás pueden quedar como colaboradores en **Settings › Collaborators**.
2. Arriba a la derecha pulsa **+** › **New repository**.
3. Escribe el nombre del proyecto sin espacios (por ejemplo, prediccion-desercion), elige la visibilidad que permita compartir los datos de tu proyecto, activa **Add README** y selecciona una licencia compatible con el código y las fuentes que uses. Pulsa **Create repository**.

## B. Organiza la carpeta del proyecto en tu computador

Crea una carpeta con el nombre del proyecto y, dentro, estas subcarpetas. Puedes dejarlas vacías hasta que las uses.

```text
nombre-del-proyecto/
├── README.md              objetivo, datos, cómo reproducir y resultados principales
├── notebooks/             los cuadernos de Colab (Hito1, Hito2, Hito3)
├── data/
│   ├── raw/               copia de los datos descargados, con fecha
│   └── processed/         datos limpios listos para modelar
├── results/
│   ├── tables/            tablas en CSV (métricas, hiperparámetros, pruebas)
│   ├── figures/           figuras en PNG a 300 dpi y en SVG
│   └── experiments.csv    una fila por corrida: fecha, modelo, parámetros, semilla y métricas
├── models/                modelo final y model_card.md
├── requirements.txt       versiones exactas de las librerías
└── LICENSE
```

- Desarrolla tu proyecto en [Google Colab](https://colab.research.google.com) con tu cuenta de Google, un cuaderno por hito: Hito1, Hito2 y Hito3. Descárgalo con **Archivo › Descargar › Descargar .ipynb** y guárdalo en notebooks.
- Para requirements.txt, ejecuta en una celda de Colab `!pip freeze > requirements.txt` y descarga el archivo desde el panel Archivos (ícono de carpeta).
- GitHub crea el README en el paso A; añade una licencia cuando hayas definido las condiciones de reutilización. Completa el README con el objetivo, los datos, cómo reproducir los resultados, los resultados principales y el **entorno de cómputo**: versión de Python, librerías y versiones (requirements.txt), tipo de máquina de Colab (CPU o GPU) y tiempo de entrenamiento de cada modelo.

## C. Cada vez que avances: sube los archivos desde la página

1. Abre tu repositorio en GitHub y pulsa **Add file** › **Upload files**.
2. Arrastra a la página la carpeta del proyecto completa o los archivos nuevos. GitHub conserva las subcarpetas.
3. Abajo, en el mensaje, escribe qué subiste (por ejemplo, «EDA del Hito 1») y pulsa **Commit changes**.

- Si subes un archivo con el mismo nombre, GitHub lo reemplaza y guarda la versión anterior en el historial.
- Desde la página se pueden subir hasta 100 archivos a la vez, de máximo 25 MB cada uno. Si tus datos pesan más, deja en data/raw solo el código de descarga y el enlace a la fuente. Si los datos son confidenciales, publica una versión anonimizada o una muestra sintética.
- Atajo opcional: en Colab, **Archivo › Guardar una copia en GitHub** guarda el cuaderno directamente en la carpeta notebooks (la primera vez te pide autorizar tu cuenta).

## D. Al cerrar cada hito: crea la versión de la entrega

La versión (en GitHub se llama *release* y su nombre es la *etiqueta* o *tag*) es una foto de tu repositorio el día de la entrega. Se crea desde la página, en un minuto:

1. En tu repositorio, en la columna de la derecha, pulsa **Releases** y luego **Draft a new release** (o **Create a new release**).
2. En **Choose a tag** escribe la versión de la entrega (por ejemplo, v0.1) y pulsa **Create new tag**.
3. En **Release title** escribe, por ejemplo, «Entrega Hito 1».
4. Pulsa **Publish release**.

| Entrega | Versión (etiqueta) |
| --- | --- |
| Hito 1 | v0.1 |
| Hito 2 | v0.2 |
| Hito 3 | v1.0 |

Si corriges algo antes del cierre, sube los cambios y crea otra versión (por ejemplo, v0.1.1).

## E. Comparte y pega los enlaces

1. En Colab: **Compartir** › Acceso general: **Cualquier persona que tenga el vínculo** › **Lector** › **Copiar vínculo**.
2. En el medio acordado con tu director comparte: Colab: [enlace] · GitHub: [enlace del repositorio] · Etiqueta: v0.1 (o la que corresponda).
3. Pega los mismos enlaces en la sección «Disponibilidad de datos y código» de tu documento.

## Opcional: GitHub Desktop (programa de escritorio, sin comandos)

1. Instala [GitHub Desktop](https://desktop.github.com) e inicia sesión con tu cuenta.
2. **File** › **Clone repository** y elige tu repositorio: queda una carpeta sincronizada en tu computador.
3. Copia tus archivos en esa carpeta. GitHub Desktop muestra los cambios: escribe un resumen, pulsa **Commit to main** y luego **Push origin**.
4. Por esta vía puedes subir archivos de hasta 100 MB. La versión de cada entrega créala igual desde la página (paso D).

## Opcional: obtén un DOI para tu repositorio (Zenodo)

El DOI es un enlace permanente a una copia de tu repositorio: tu trabajo queda disponible y se puede citar aunque después cambies o borres el repositorio. Es opcional y se hace desde la página, sin comandos.

1. Entra a [zenodo.org](https://zenodo.org), pulsa **Log in** y elige entrar con **GitHub**.
2. En el menú de tu perfil (arriba a la derecha), elige **GitHub** y pulsa **Sync now**.
3. Busca tu repositorio y activa su interruptor.
4. En GitHub, crea la versión v1.0 (paso D). Zenodo la archiva y le asigna un DOI en pocos minutos. Si ya habías creado la v1.0 antes de activar Zenodo, crea una nueva versión (por ejemplo, v1.0.1).
5. Copia el DOI en el README y en la sección «Disponibilidad de datos y código» de tu documento.

## Reproducibilidad

- Fija la semilla y guarda las versiones de las librerías (requirements.txt) para que cualquier tabla o figura se regenere igual.
- El cuaderno corre de principio a fin sin errores.
- Ninguna cifra del documento se escribe a mano: todas salen de results/tables.

[Volver al inicio](../README.md)

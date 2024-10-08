
# FastAPI-Renacyt

Este proyecto `FastAPI-Renacyt` es una API diseñada para gestionar y procesar datos eficientemente utilizando FastAPI. Está optimizado para ofrecer respuestas rápidas y manejar solicitudes concurrentes, facilitando la integración con sistemas de bases de datos y servicios externos.

## Requisitos previos

Para ejecutar este proyecto, asegúrate de tener instalados los siguientes programas:

- Python 3.10
- Git

## Instalación

A continuación, se detallan los pasos para configurar y ejecutar el proyecto localmente.

### 1. Clonación del repositorio

Primero, clona el repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/AxelValuis/DemoConcytecBackend.git
cd FastAPI-Renacyt
```

### 2. Configuración del entorno virtual

Es recomendable usar un entorno virtual para manejar las dependencias del proyecto de manera aislada. Para crear y activar un entorno virtual, sigue estos pasos:

#### En Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### En macOS y Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Instalación de dependencias

Con el entorno virtual activado, instala todas las dependencias necesarias para el proyecto ejecutando:

```bash
pip install -r requirements.txt
```


### 5. Ejecución del proyecto

Para iniciar el servidor de desarrollo y acceder a la aplicación, ejecuta:

```bash
uvicorn main:app --reload
```

Este comando asume que tu archivo principal se llama `main.py` y que la instancia de la aplicación FastAPI se llama `app`.


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` en el repositorio para más detalles.

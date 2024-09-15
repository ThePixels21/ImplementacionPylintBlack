"""
Módulo principal de la aplicación FastAPI que configura la conexión a la base de datos,
gestiona el ciclo de vida de la aplicación y define las rutas principales.
"""

# Importación del manejador de contexto asíncrono
from contextlib import asynccontextmanager

# Importación de FastAPI y RedirectResponse para gestionar las redirecciones
from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Importación de la conexión a la base de datos y de las rutas del módulo de proyectos
from database import database as connection
from routes.project_route import project_route


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Gestor de ciclo de vida para la aplicación FastAPI que maneja la conexión
    a la base de datos al iniciar y finalizar la aplicación.

    Parámetros:
    -----------
    app : FastAPI
        La instancia de la aplicación FastAPI.

    Yields:
    -------
    None
        Permite que la aplicación se ejecute dentro del contexto establecido.
    """
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí se ejecuta la aplicación dentro del ciclo de vida
    finally:
        # Cerrar la conexión a la base de datos cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


# Creación de la instancia de la aplicación FastAPI con la configuración de ciclo de vida
app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    """
    Redirecciona la ruta raíz ("/") hacia la documentación interactiva de la API.

    Retorna:
    --------
    RedirectResponse:
        Una respuesta que redirige a "/docs", que es la interfaz de documentación de FastAPI.
    """
    return RedirectResponse(url="/docs")


# Incluir las rutas del módulo de proyectos bajo el prefijo "/api/projects"
app.include_router(project_route, prefix="/api/projects", tags=["projects"])

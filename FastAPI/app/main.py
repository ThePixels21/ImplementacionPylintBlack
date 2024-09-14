from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from database import database as connection
from routes.user_route import user_route
from routes.cinema_route import cinema_route
from routes.movie_route import movie_route
from routes.snack_route import snack_route
from routes.theater_route import theater_route
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/api/users", tags=["Users"])
app.include_router(cinema_route, prefix = "/api/cinemas", tags = ["Cinemas"])
app.include_router(movie_route, prefix = "/api/movies", tags = ["Movies"])
app.include_router(snack_route, prefix = "/api/snacks", tags = ["Snacks"])
app.include_router(theater_route, prefix = "/api/theaters", tags = ["Theaters"])

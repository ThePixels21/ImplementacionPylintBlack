"""
Main module for FastAPI application setup.

This module sets up the FastAPI application, manages the database connection
lifecycle, and includes routes.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from database import database as connection
from routes.employee_route import employee_route
from routes.proyect_route import project_route

@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    Ensures the database connection is opened and closed properly.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=manage_lifespan)

@app.get("/")
async def read_root():
    """
    Redirect the root path to the API documentation.

    Returns a redirection response to the documentation page.
    """
    return RedirectResponse(url="/docs")

app.include_router(employee_route, prefix="/api/employees", tags=["Employees"])
app.include_router(project_route, prefix="/api/projects", tags=["projects"])

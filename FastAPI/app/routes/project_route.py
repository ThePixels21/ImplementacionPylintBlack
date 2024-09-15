"""
Este módulo define las rutas de la API para gestionar proyectos utilizando FastAPI y Peewee ORM.
Permite obtener, crear, actualizar y eliminar proyectos en la base de datos.
"""

# Importar APIRouter de FastAPI para crear rutas
from fastapi import APIRouter, Body, HTTPException

# Importar el modelo de datos Project de Pydantic
from models.project import Project

# Importar el modelo de base de datos ProjectModel
from database import ProjectModel

# Crear una instancia de APIRouter para las rutas del proyecto
project_route = APIRouter()


@project_route.get("/")
def get_all_projects():
    """
    Obtiene todos los proyectos almacenados en la base de datos.

    Retorna:
    --------
    list:
        Una lista con todos los proyectos.
    dict:
        En caso de error, retorna un diccionario con el mensaje de error.
    """
    projects = list(ProjectModel.select())  # Selecciona todos los proyectos
    return projects

@project_route.get("/{project_id}")
def get_project(project_id: int):
    """
    Obtiene un proyecto específico según su ID.

    Parámetros:
    -----------
    projectId : int
        El ID del proyecto a obtener.

    Retorna:
    --------
    ProjectModel:
        El proyecto con el ID especificado.
    dict:
        En caso de error, retorna un diccionario con el mensaje de error.
    """
    try:
        project = ProjectModel.get(ProjectModel.id == project_id)  # Obtener proyecto por ID
        return project
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Project no encontrado") from exc


@project_route.post("/")
def create_project(project: Project = Body(...)):
    """
    Crea un nuevo proyecto y lo almacena en la base de datos.

    Parámetros:
    -----------
    project : Proyect
        El proyecto a crear, proporcionado en el cuerpo de la solicitud.

    Retorna:
    --------
    Proyect:
        El proyecto creado.
    dict:
        En caso de error, retorna un diccionario con el mensaje de error.
    """
    ProjectModel.create(
        name=project.name,
        description=project.description,
        init_date=project.init_date,
        finish_date=project.finish_date
    )
    return project

@project_route.put("/{project_id}")
def update_project(project_id: int, project: Project = Body(...)):
    """
    Actualiza un proyecto existente en la base de datos.

    Parámetros:
    -----------
    projectId : int
        El ID del proyecto a actualizar.
    project : Proyect
        Los nuevos datos del proyecto, proporcionados en el cuerpo de la solicitud.

    Retorna:
    --------
    str:
        Un mensaje que indica si el proyecto fue actualizado exitosamente.
    dict:
        En caso de error, retorna un diccionario con el mensaje de error.
    """
    try:
        e_project = ProjectModel.get(ProjectModel.id == project_id)  # Obtener proyecto existente

        e_project.name = project.name
        e_project.description = project.description
        e_project.init_date = project.init_date
        e_project.finish_date = project.finish_date

        e_project.save()  # Guardar cambios
        return "Project updated successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Projecto no encontrado") from exc

@project_route.delete("/{project_id}")
def delete_project(project_id: int):
    """
    Elimina un proyecto de la base de datos según su ID.

    Parámetros:
    -----------
    projectId : int
        El ID del proyecto a eliminar.

    Retorna:
    --------
    str:
        Un mensaje que indica si el proyecto fue eliminado exitosamente.
    dict:
        En caso de error, retorna un diccionario con el mensaje de error.
    """
    try:
        project = ProjectModel.get(ProjectModel.id == project_id)  # Obtener proyecto por ID

        project.delete_instance()  # Eliminar proyecto
        return "Project deleted successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Proyecto no encontrado") from exc

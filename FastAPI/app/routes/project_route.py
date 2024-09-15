"""
Este módulo define las rutas de la API para gestionar proyectos utilizando FastAPI y Peewee ORM.
Permite obtener, crear, actualizar y eliminar proyectos en la base de datos.
"""

# Importar APIRouter de FastAPI para crear rutas
from fastapi import APIRouter, Body

# Importar el modelo de datos Project de Pydantic
from FastAPI.app.models.project import Proyect

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
    try:
        projects = list(ProjectModel.select())  # Selecciona todos los proyectos
        return projects
    except Exception as e:
        print(e)
        return {"error": str(e)}


@project_route.get("/{projectId}")
def get_project(projectId: int):
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
        project = ProjectModel.get(ProjectModel.id == projectId)  # Obtener proyecto por ID
        return project
    except Exception as e:
        print(e)
        return {"error": str(e)}


@project_route.post("/")
def create_project(project: Proyect = Body(...)):
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
    try:
        ProjectModel.create(
            name=project.name,
            description=project.description,
            init_date=project.init_date,
            finish_date=project.finish_date
        )
        return project
    except Exception as e:
        print(e)
        return {"error": str(e)}


@project_route.put("/{projectId}")
def update_project(projectId: int, project: Proyect = Body(...)):
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
        existing_project = ProjectModel.get(ProjectModel.id == projectId)  # Obtener proyecto existente

        if existing_project is None:
            return "The project doesn't exist"
        else:
            # Actualizar campos del proyecto
            existing_project.name = project.name
            existing_project.description = project.description
            existing_project.init_date = project.init_date
            existing_project.finish_date = project.finish_date

            existing_project.save()  # Guardar cambios
            return "Project updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}


@project_route.delete("/{projectId}")
def delete_project(projectId: int):
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
        project = ProjectModel.get(ProjectModel.id == projectId)  # Obtener proyecto por ID
        if project is None:
            return "The project doesn't exist"
        else:
            project.delete_instance()  # Eliminar proyecto
            return "Project deleted successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

# Fin del archivo

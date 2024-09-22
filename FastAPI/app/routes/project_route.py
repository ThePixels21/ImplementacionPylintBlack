"""
This module defines the API routes to manage projects using FastAPI and Peewee ORM.
It allows fetching, creating, updating, and deleting projects in the database.
"""

# Import APIRouter from FastAPI to create routes
from fastapi import APIRouter, Body

# Import the Project data model from Pydantic
from models.project import Project

from services.project_service import ProjectService

# Create an instance of APIRouter for project routes
project_route = APIRouter()

@project_route.get("/")
def get_all_projects():
    """
    Retrieves all the projects stored in the database.

    Returns:
    --------
    list:
        A list of all projects.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return ProjectService.get_all_projects()

@project_route.get("/{project_id}")
def get_project(project_id: int):
    """
    Retrieves a specific project by its ID.

    Parameters:
    -----------
    projectId : int
        The ID of the project to retrieve.

    Returns:
    --------
    ProjectModel:
        The project with the specified ID.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return ProjectService.get_project(project_id)

@project_route.post("/")
def create_project(project: Project = Body(...)):
    """
    Creates a new project and stores it in the database.

    Parameters:
    -----------
    project : Project
        The project to create, provided in the request body.

    Returns:
    --------
    Project:
        The created project.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return ProjectService.create_project(project)

@project_route.put("/{project_id}")
def update_project(project_id: int, project: Project = Body(...)):
    """
    Updates an existing project in the database.

    Parameters:
    -----------
    projectId : int
        The ID of the project to update.
    project : Project
        The new data for the project, provided in the request body.

    Returns:
    --------
    str:
        A message indicating if the project was successfully updated.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return ProjectService.update_project(project_id,project)

@project_route.delete("/{project_id}")
def delete_project(project_id: int):
    """
    Deletes a project from the database by its ID.

    Parameters:
    -----------
    projectId : int
        The ID of the project to delete.

    Returns:
    --------
    str:
        A message indicating if the project was successfully deleted.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return ProjectService.delete_project(project_id)

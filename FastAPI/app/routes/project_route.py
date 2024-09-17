"""
This module defines the API routes to manage projects using FastAPI and Peewee ORM.
It allows fetching, creating, updating, and deleting projects in the database.
"""

# Import APIRouter from FastAPI to create routes
from fastapi import APIRouter, Body, HTTPException

# Import the Project data model from Pydantic
from models.project import Project

# Import the ProjectModel database model
from database import ProjectModel

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
    projects = list(ProjectModel.select())  # Select all projects
    return projects

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
    try:
        project = ProjectModel.get(ProjectModel.id == project_id)  # Get project by ID
        return project
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Project not found") from exc

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
    try:
        e_project = ProjectModel.get(ProjectModel.id == project_id)  # Get existing project

        e_project.name = project.name
        e_project.description = project.description
        e_project.init_date = project.init_date
        e_project.finish_date = project.finish_date

        e_project.save()  # Save changes
        return "Project updated successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Project not found") from exc

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
    try:
        project = ProjectModel.get(ProjectModel.id == project_id)  # Get project by ID

        project.delete_instance()  # Delete project
        return "Project deleted successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Project not found") from exc

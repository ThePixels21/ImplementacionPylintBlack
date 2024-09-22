"""
Module to handle project-related business logic for managing projects.

This module defines the `ProjectService` class, which provides methods
for creating, retrieving, updating, and deleting projects from the database.
It interacts with the ProjectModel to persist and manage project data.
"""
from peewee import DoesNotExist, IntegrityError  # type: ignore

from fastapi import Body, HTTPException

from models.project import Project

# Import the ProjectModel database model
from database import ProjectModel


class ProjectService:
    """
    Service class for handling business logic related to projects.

    This class provides methods to interact with the project data stored in the database.
    It encapsulates common operations such as retrieving, creating, updating, and deleting projects.

    Methods:
        create_project(project: Project)
            Creates a new project in the database.

        update_project(project_id: int, project: Project)
            Updates an existing project with the given ID in the database.

        delete_project(project_id: int)
            Deletes a project from the database by its ID.

        get_project(project_id: int)
            Retrieves a project by its ID from the database.

        get_all_projects()
            Retrieves all projects from the database.

    Raises:
        ValueError
            If any provided data for project creation or update is invalid.
        IntegrityError
            If there is a database integrity issue during project creation or update.
        DoesNotExist
            If no project with the given ID exists.
        HTTPException
            If there's an HTTP-related error during the operation (e.g., project not found).
    """
    @staticmethod
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

    @staticmethod
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
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="Project not found") from exc

    @staticmethod
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
        try:
            ProjectModel.create(
                name=project.name,
                description=project.description,
                init_date=project.init_date,
                finish_date=project.finish_date
            )
            return project
        except DoesNotExist as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except IntegrityError as exc:
            raise HTTPException(
            status_code=500, detail="An error occurred while creating the project"
        ) from exc

    @staticmethod
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
        except Exception as exc:  
            raise HTTPException(status_code=404, detail="Project not found") from exc

    @staticmethod
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
        except DoesNotExist as exc:  # Catching general exception if DoesNotExist is not available
            raise HTTPException(status_code=404, detail="Project not found") from exc

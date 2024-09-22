"""
This module defines the API routes to manage tasks using FastAPI and Peewee ORM.
It allows fetching, creating, updating, and deleting tasks in the database.
"""

# Import APIRouter from FastAPI to create routes
from fastapi import APIRouter, Body

# Import the Task data model from Pydantic
from models.task import Task

from services.task_service import TaskService

# Create an instance of APIRouter for task routes
task_route = APIRouter()

@task_route.get("/")
def get_all_tasks():
    """
    Retrieves all the tasks stored in the database.

    Returns:
    --------
    list:
        A list of all tasks.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return TaskService.get_all_tasks()

@task_route.get("/{task_id}")
def get_task(task_id: int):
    """
    Retrieves a specific task by its ID.

    Parameters:
    -----------
    task_id : int
        The ID of the task to retrieve.

    Returns:
    --------
    TaskModel:
        The task with the specified ID.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return TaskService.get_task(task_id)

@task_route.post("/")
def create_task(task: Task = Body(...)):
    """
    Creates a new task and stores it in the database.

    Parameters:
    -----------
    task : Task
        The task to create, provided in the request body.

    Returns:
    --------
    Task:
        The created task.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return TaskService.create_task(task)

@task_route.put("/{task_id}")
def update_task(task_id: int, task: Task = Body(...)):
    """
    Updates an existing task in the database.

    Parameters:
    -----------
    task_id : int
        The ID of the task to update.
    task : Task
        The new data for the task, provided in the request body.

    Returns:
    --------
    str:
        A message indicating if the task was successfully updated.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return TaskService.update_task(task_id,task)

@task_route.delete("/{task_id}")
def delete_task(task_id: int):
    """
    Deletes a task from the database by its ID.

    Parameters:
    -----------
    task_id : int
        The ID of the task to delete.

    Returns:
    --------
    str:
        A message indicating if the task was successfully deleted.
    dict:
        In case of error, returns a dictionary with the error message.
    """
    return TaskService.delete_task(task_id)

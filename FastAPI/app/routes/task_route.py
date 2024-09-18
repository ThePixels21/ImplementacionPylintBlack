"""
This module defines the API routes to manage tasks using FastAPI and Peewee ORM.
It allows fetching, creating, updating, and deleting tasks in the database.
"""

# Import APIRouter from FastAPI to create routes
from fastapi import APIRouter, Body, HTTPException

# Import the Task data model from Pydantic
from models.task import Task

# Import the TaskModel database model
from database import TaskModel

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
    tasks = list(TaskModel.select())  # Select all tasks
    return tasks

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
    try:
        task = TaskModel.get(TaskModel.id == task_id)  # Get task by ID
        return task
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Task not found") from exc

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
    TaskModel.create(
        project_id=task.project_id,
        employee_id=task.employee_id,
        title=task.title,
        description=task.description,
        deadline=task.deadline,
        status=task.status
    )
    return task

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
    try:
        e_task = TaskModel.get(TaskModel.id == task_id)  # Get existing task

        e_task.project_id = task.project_id
        e_task.employee_id = task.employee_id
        e_task.title = task.title
        e_task.description = task.description
        e_task.deadline = task.deadline
        e_task.status = task.status

        e_task.save()  # Save changes
        return "Task updated successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Task not found") from exc

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
    try:
        task = TaskModel.get(TaskModel.id == task_id)  # Get task by ID

        task.delete_instance()  # Delete task
        return "Task deleted successfully"
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Task not found") from exc

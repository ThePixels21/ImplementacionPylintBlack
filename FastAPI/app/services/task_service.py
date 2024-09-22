"""
This module provides services to manage tasks in the database.

It includes functionalities for retrieving, creating, updating, and deleting tasks.
"""
from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.task import Task
from database import TaskModel

class TaskService:
    """
    Service class for handling business logic related to tasks.

    This class provides methods to manage tasks, such as retrieving all tasks,
    getting a specific task by ID, creating, updating, and deleting tasks in the database.
    
    Methods:
        get_all_tasks()
            Retrieves all the tasks from the database.
            
        get_task(task_id: int)
            Retrieves a specific task by its ID.
            
        create_task(task: Task)
            Creates a new task and stores it in the database.
            
        update_task(task_id: int, task: Task)
            Updates an existing task in the database.
            
        delete_task(task_id: int)
            Deletes a task from the database by its ID.

    Raises:
        HTTPException
            If a task is not found or if there is an error during any operation.
    """
    @staticmethod
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

    @staticmethod
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
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="Task not found") from exc

    @staticmethod
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
        try:
            TaskModel.create(
                project_id=task.project_id,
                employee_id=task.employee_id,
                title=task.title,
                description=task.description,
                deadline=task.deadline,
                status=task.status
            )
            return task
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except IntegrityError as exc:
            raise HTTPException(
            status_code=500, detail="An error occurred while creating the project"
        ) from exc

    @staticmethod
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
        except DoesNotExist as exc:  # Catching general exception if DoesNotExist is not available
            raise HTTPException(status_code=404, detail="Task not found") from exc

    @staticmethod
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
        except DoesNotExist as exc:  # Catching general exception if DoesNotExist is not available
            raise HTTPException(status_code=404, detail="Task not found") from exc

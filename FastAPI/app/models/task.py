"""
Module that defines the `Task` data model using Pydantic. This model
represents a task that has an associated project, an assigned employee,
title, description, deadline, and status.
"""

# Import the date class to handle dates
from datetime import date

# Import BaseModel from Pydantic to create the data model
from pydantic import BaseModel


class Task(BaseModel):
    """
    `Task` data model that validates task information.

    Attributes:
    ----------
    project_id : int
        Identifier of the project associated with the task.
    employee_id : int
        Identifier of the employee assigned to the task.
    title : str
        Title of the task.
    description : str
        Detailed description of the task.
    limit_date : date
        Deadline for completing the task.
    status : bool, optional
        Status of the task, default is `False` (pending).
    """
    project_id: int
    employee_id: int
    title: str
    description: str
    limit_date: date
    status: bool = False  # Default status is `False` (pending task)

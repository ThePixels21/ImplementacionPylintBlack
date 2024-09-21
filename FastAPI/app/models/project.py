"""
Module that defines the Project data model using Pydantic for data validation
in FastAPI. This model represents a project with its name, description,
start date, and end date.
"""

# Import the date class to handle dates
from datetime import date
# Import BaseModel from Pydantic to create the data model
from pydantic import BaseModel


class Project(BaseModel):
    """
    Project data model that validates project information.

    Attributes:
    ----------
    name : str
        Name of the project.
    description : str
        Brief description of the project.
    init_date : date
        Start date of the project.
    finish_date : date
        End date of the project.
    """

    name: str
    description: str
    init_date: date
    finish_date: date

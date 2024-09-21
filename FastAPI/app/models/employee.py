"""
This module defines the Pydantic model for an employee.

The `Employee` class represents an employee and includes attributes
such as id, name, email, phone, and post. This model is used for
data validation and serialization within the application.
"""

from pydantic import BaseModel

class Employee(BaseModel):
    """
    A Pydantic model representing an employee.

    Attributes:
        name (str): The name of the employee.
        email (str): The email address of the employee.
        phone (str): The phone number of the employee.
        post (str): The job position or title of the employee.
    """

    name: str
    email: str
    phone: str
    post: str

"""
This module defines the API routes for employee management.

Routes provided:
- GET /employees: Retrieve a list of all employees.
- GET /employees/{employee_id}: Retrieve a specific employee by ID.
- POST /employees: Create a new employee record.
- PUT /employees/{employee_id}: Update an existing employee record by ID.
- DELETE /employees/{employee_id}: Delete an employee record by ID.
"""

from fastapi import APIRouter, Body
from models.employee import Employee
from database import EmployeeModel
from peewee import DoesNotExist
from starlette.exceptions import HTTPException

employee_route = APIRouter()

@employee_route.get("/employees")
def get_employees():
    """
    Retrieve a list of all employees.

    Returns:
        List[Employee]: A list of all employee records in the database.
    """
    employees = list(EmployeeModel.select())
    return employees

@employee_route.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    """
    Retrieve a specific employee by their ID.

    Args:
        employee_id (int): The ID of the employee to retrieve.

    Returns:
        Employee: The employee record with the specified ID.

    Raises:
        HTTPException: 404 error if the employee with the given ID is not found.
    """
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employee_id)
        return employee
    except DoesNotExist as exc:
        raise HTTPException(404, "Employee not found") from exc

@employee_route.post("/employees")
def create_employee(employee: Employee = Body(...)):
    """
    Create a new employee record.

    Args:
        employee (Employee): The employee data to create.

    Returns:
        Employee: The newly created employee record.
    """
    EmployeeModel.create(
        name=employee.name,
        email=employee.email,
        phone=employee.phone,
        post=employee.post
    )
    return employee

@employee_route.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee_data: dict):
    """
    Update an existing employee record by their ID.

    Args:
        employee_id (int): The ID of the employee to update.
        employee_data (dict): The new data for the employee.

    Returns:
        dict: A message indicating the result of the update operation.

    Note:
        The actual implementation of this method is pending.
    """
    raise HTTPException(501, "Not implemented")

@employee_route.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    """
    Delete an employee record by their ID.

    Args:
        employee_id (int): The ID of the employee to delete.

    Returns:
        dict: A message indicating the result of the delete operation.

    Raises:
        HTTPException: 404 error if the employee with the given ID is not found.
    """
    try:
        EmployeeModel.delete().where(EmployeeModel.id == employee_id).execute()
        return {"status": "Employee deleted"}
    except DoesNotExist as exc:
        raise HTTPException(404, "Employee not found") from exc

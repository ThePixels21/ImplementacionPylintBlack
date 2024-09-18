"""
This module defines the API routes for employee management.

Routes provided:
- GET /employees: Retrieve a list of all employees.
- GET /employees/{employee_id}: Retrieve a specific employee by ID.
- POST /employees: Create a new employee record.
- PUT /employees/{employee_id}: Update an existing employee record by ID.
- DELETE /employees/{employee_id}: Delete an employee record by ID.
"""

from typing import List, Dict
from fastapi import APIRouter, Body, HTTPException
from models.employee import Employee
from database import EmployeeModel

employee_route = APIRouter()

@employee_route.get("/")
def get_employees():
    """
    Retrieve a list of all employees.

    Returns:
        List[Employee]: A list of all employee records in the database.
    """
    employees = list(EmployeeModel.select())
    return employees

@employee_route.get("/{employee_id}")
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
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Employee not found") from exc

@employee_route.post("/")
def create_employee(employee: Employee = Body(...)):
    """
    Create a new employee record.

    Args:
        employee (Employee): The employee data to create.

    Returns:
        Employee: The newly created employee record.
    """
    created_employee = EmployeeModel.create(
        name=employee.name,
        email=employee.email,
        phone=employee.phone,
        post=employee.post
    )
    return created_employee

@employee_route.put("/{employee_id}")
def update_employee(employee_id: int, employee_data: Dict[str, str]):
    """
    Update an existing employee record by their ID.

    Args:
        employee_id (int): The ID of the employee to update.
        employee_data (Dict[str, str]): The new data for the employee.

    Returns:
        Employee: The updated employee record.

    Raises:
        HTTPException: 404 error if the employee with the given ID is not found.
    """
    try:
        employee = EmployeeModel.get(EmployeeModel.id == employee_id)
        employee.name = employee_data.get("name", employee.name)
        employee.email = employee_data.get("email", employee.email)
        employee.phone = employee_data.get("phone", employee.phone)
        employee.post = employee_data.get("post", employee.post)
        employee.save()
        return employee
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Employee not found") from exc

@employee_route.delete("/{employee_id}")
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
    except Exception as exc:  # Catching general exception if DoesNotExist is not available
        raise HTTPException(status_code=404, detail="Employee not found") from exc

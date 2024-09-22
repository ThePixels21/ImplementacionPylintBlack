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
from services.employee_service import EmployeeService

employee_route = APIRouter()

@employee_route.get("/")
def get_employees():
    """
    Retrieve a list of all employees.

    Returns:
        List[Employee]: A list of all employee records in the database.
    """
    return EmployeeService.get_employees()

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
    return EmployeeService.get_employee(employee_id)

@employee_route.post("/")
def create_employee(employee: Employee = Body(...)):
    """
    Create a new employee record.

    Args:
        employee (Employee): The employee data to create.

    Returns:
        Employee: The newly created employee record.
    """
    return EmployeeService.create_employee(employee)

@employee_route.put("/{employee_id}")
def update_employee(employee_id: int, employee: Employee = Body(...)):
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
    return EmployeeService.update_employee(employee_id,employee)

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
    return EmployeeService.delete_employee(employee_id)

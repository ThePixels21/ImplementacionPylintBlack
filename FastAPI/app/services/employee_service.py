"""
This module provides a service class for managing employee-related operations,
including retrieving, creating, updating, and deleting employee records from the database.
"""

from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.employee import Employee
from database import EmployeeModel


class EmployeeService:
    """
    Service class for handling business logic related to employees.

    This class provides methods to manage employee records, including operations
    such as creating, updating, retrieving, and deleting employee information
    from the database.

    Methods:
        get_employees()
            Retrieve a list of all employees.
        
        get_employee(employee_id: int)
            Retrieve a specific employee by their ID.
        
        create_employee(employee: Employee)
            Create a new employee record.
        
        update_employee(employee_id: int, employee_data: Dict[str, str])
            Update an existing employee record by their ID.
        
        delete_employee(employee_id: int)
            Delete an employee record by their ID.

    Raises:
        HTTPException
            If an employee is not found or if there is an error during any operation.
    """
    @staticmethod
    def get_employees():
        """
        Retrieve a list of all employees.

        Returns:
            List[Employee]: A list of all employee records in the database.
        """
        employees = list(EmployeeModel.select())
        return employees

    @staticmethod
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
            raise HTTPException(status_code=404, detail="Employee not found") from exc

    @staticmethod
    def create_employee(employee: Employee = Body(...)):
        """
        Create a new employee record.

        Args:
            employee (Employee): The employee data to create.

        Returns:
            Employee: The newly created employee record.
        """
        try:
            created_employee = EmployeeModel.create(
                name=employee.name,
                email=employee.email,
                phone=employee.phone,
                post=employee.post
            )
            return created_employee
        except DoesNotExist as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except IntegrityError as exc:
            raise HTTPException(
            status_code=500, detail="An error occurred while creating the employee"
        ) from exc

    @staticmethod
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
        try:
            e_employee = EmployeeModel.get(EmployeeModel.id == employee_id)
            e_employee.name = employee.name
            e_employee.email = employee.email
            e_employee.phone = employee.phone
            e_employee.post = employee.post
            e_employee.save()
            return e_employee
        except DoesNotExist as exc:  # Catching general exception if DoesNotExist is not available
            raise HTTPException(status_code=404, detail="Employee not found") from exc

    @staticmethod
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
        except DoesNotExist as exc:  # Catching general exception if DoesNotExist is not available
            raise HTTPException(status_code=404, detail="Employee not found") from exc

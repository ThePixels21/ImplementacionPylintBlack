"""
This module configures the MySQL database connection and defines
the Peewee model for interacting with the 'employees' table.
"""

import os
from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, DateField, AutoField, CharField, ForeignKeyField

# Load environment variables from a .env file
load_dotenv()

# Configure the MySQL database connection
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class EmployeeModel(Model):
    """
    Peewee model representing an employee in the database.

    Attributes:
        id (AutoField): The unique identifier of the employee (auto-incremented primary key).
        name (CharField): The name of the employee (up to 50 characters).
        email (CharField): The email address of the employee (up to 50 characters).
        phone (CharField): The phone number of the employee (up to 50 characters).
        post (CharField): The job position or title of the employee (up to 50 characters).
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=50)
    post = CharField(max_length=50)

    class Meta:
        """
        Metadata for the EmployeeModel.

        Attributes:
            database (MySQLDatabase): The database connection to use for this model.
            table_name (str): The name of the table in the database to which this model is mapped.
        """
        # pylint: disable=too-few-public-methods
        database = database
        table_name = "employees"

class ProjectModel(Model):
    """
    Model that represents the 'projects' table in the database.

    Attributes:
    ----------
    id : AutoField
        Auto-incremental field that serves as the unique identifier of the project.
    name : CharField
        String field that stores the name of the project (max. 50 characters).
    description : CharField
        String field that stores a description of the project (max. 50 characters).
    init_date : DateField
        Field that stores the start date of the project.
    finish_date : DateField
        Field that stores the end date of the project.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    init_date = DateField()
    finish_date = DateField()

    class Meta:
        """
        Meta class that defines the additional configuration of the model.

        Attributes:
        ----------
        database : MySQLDatabase
            The database to which the model is linked.
        table_name : str
            Name of the table in the database that represents this model.
        """
        # pylint: disable=too-few-public-methods
        database = database
        table_name = "projects"

class TaskModel(Model):
    """
    Model that represents the 'tasks' table in the database.

    Attributes:
    ----------
    id : AutoField
        Auto-incremental field that serves as the unique identifier of the task.
    project_id : ForeignKeyField
        Foreign key that links the task to a project.
    employee_id : ForeignKeyField
        Foreign key that links the task to an employee.
    title : CharField
        String field that stores the title of the task (max. 50 characters).
    description : TextField
        Text field that stores a detailed description of the task.
    deadline : DateField
        Field that stores the deadline date of the task.
    status : CharField
        String field that stores the current status of the task (max. 20 characters).
    """
    id = AutoField(primary_key=True)
    project_id = ForeignKeyField(ProjectModel, backref='tasks', on_delete='CASCADE')
    employee_id = ForeignKeyField(EmployeeModel, backref='tasks', on_delete='CASCADE')
    title = CharField(max_length=50)
    description = CharField(max_length=500)
    deadline = DateField()
    status = CharField(max_length=20)

    class Meta:
        """
        Meta class that defines the additional configuration of the model.

        Attributes:
        ----------
        database : MySQLDatabase
            The database to which the model is linked.
        table_name : str
            Name of the table in the database that represents this model.
        """
        # pylint: disable=too-few-public-methods
        database = database
        table_name = "tasks"

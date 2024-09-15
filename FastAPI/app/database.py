"""
This module configures the MySQL database connection and defines
the Peewee model for interacting with the 'employees' table.
"""

import os
from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, DateField,AutoField, CharField

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
    Modelo que representa la tabla 'projects' en la base de datos.

    Atributos:
    ----------
    id : AutoField
        Campo autoincremental que sirve como identificador único del proyecto.
    name : CharField
        Campo de tipo cadena que almacena el nombre del proyecto (máx. 50 caracteres).
    description : CharField
        Campo de tipo cadena que almacena una descripción del proyecto (máx. 50 caracteres).
    init_date : DateField
        Campo que almacena la fecha de inicio del proyecto.
    finish_date : DateField
        Campo que almacena la fecha de finalización del proyecto.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    init_date = DateField()
    finish_date = DateField()

    class Meta:
        """
        Clase Meta que define la configuración adicional del modelo.

        Atributos:
        ----------
        database : MySQLDatabase
            La base de datos a la que está vinculado el modelo.
        table_name : str
            Nombre de la tabla en la base de datos que representa este modelo.
        """
        # pylint: disable=too-few-public-methods
        database = database
        table_name = "projects"

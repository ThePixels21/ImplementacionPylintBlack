"""
Módulo que establece la conexión con una base de datos MySQL usando
variables de entorno y define un modelo de proyectos utilizando Peewee ORM.
"""

# Importar las librerías necesarias
from dotenv import load_dotenv
from peewee import *
import os

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Configuración de la base de datos
# Se obtiene la configuración desde las variables de entorno usando os.getenv()
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),    # Nombre de la base de datos
    user=os.getenv("MYSQL_USER"),   # Nombre del usuario
    passwd=os.getenv("MYSQL_PASSWORD"),  # Contraseña del usuario
    host=os.getenv("MYSQL_HOST"),   # Dirección del servidor MySQL
    port=int(os.getenv("MYSQL_PORT"))    # Puerto en el que se encuentra el servidor
)

class ProjectModel(Model):
    """
    Modelo que representa la tabla 'proyects' en la base de datos.

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
        database = database
        table_name = "projects"

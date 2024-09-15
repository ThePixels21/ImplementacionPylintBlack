"""
Módulo que define el modelo de datos `Task` utilizando Pydantic. Este modelo
representa una tarea que tiene un proyecto asociado, un empleado asignado,
título, descripción, fecha límite y estado.
"""

# Importar la clase date para manejar fechas
from datetime import date

# Importar BaseModel de Pydantic para crear el modelo de datos
from pydantic import BaseModel


class Task(BaseModel):
    """
    Modelo de datos `Task` que valida la información de una tarea.

    Atributos:
    ----------
    proyect_id : int
        Identificador del proyecto al que está asociada la tarea.
    employee_id : int
        Identificador del empleado asignado a la tarea.
    tittle : str
        Título de la tarea.
    description : str
        Descripción detallada de la tarea.
    limit_date : date
        Fecha límite para completar la tarea.
    status : bool, opcional
        Estado de la tarea, por defecto es `False` (pendiente).
    """
    proyect_id: int
    employee_id: int
    tittle: str
    description: str
    limit_date: date
    status: bool = False  # Estado por defecto es `False` (tarea pendiente)

# Fin del archivo

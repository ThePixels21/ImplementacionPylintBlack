"""
Módulo que define el modelo de datos `Project` utilizando Pydantic para validación
de datos en FastAPI. Este modelo representa un proyecto con su nombre, descripción,
fecha de inicio y fecha de finalización.
"""

# Importar BaseModel de Pydantic para crear el modelo de datos
from pydantic import BaseModel

# Importar la clase date para manejar fechas
from datetime import date


class Project(BaseModel):
    """
    Modelo de datos `Project` que valida la información de un proyecto.

    Atributos:
    ----------
    name : str
        Nombre del proyecto.
    description : str
        Descripción breve del proyecto.
    init_date : date
        Fecha de inicio del proyecto.
    finish_date : date
        Fecha de finalización del proyecto.
    """
    
    name: str
    description: str
    init_date: date
    finish_date: date

# Fin del archivo
    
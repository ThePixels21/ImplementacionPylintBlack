from pydantic import BaseModel
from datetime import date

class Task (BaseModel):
    proyect_id: int
    employee_id: int
    tittle: str
    description: str
    limit_date: date
    status = False
    
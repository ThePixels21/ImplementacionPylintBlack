from pydantic import BaseModel
from datetime import date

class Project (BaseModel):
    name: str
    description: str
    init_date: date
    finish_date: date
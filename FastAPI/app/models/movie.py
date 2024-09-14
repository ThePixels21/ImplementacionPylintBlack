from datetime import datetime
from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    description: str
    actors: str
    releaseDate: datetime
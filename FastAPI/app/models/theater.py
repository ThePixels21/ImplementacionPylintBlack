from pydantic import BaseModel

class Theater(BaseModel):
    theaterNumber: int
    peopleInside: int
    playing: str
    capacity: int

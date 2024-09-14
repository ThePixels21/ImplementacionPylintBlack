from pydantic import BaseModel

class Cinema(BaseModel):
    name: str
    address: str
    theatersCount: int
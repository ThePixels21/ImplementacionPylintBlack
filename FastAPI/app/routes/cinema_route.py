from fastapi import APIRouter, Body, HTTPException
from models.cinema import Cinema
from database import CinemaModel

cinema_route = APIRouter()


@cinema_route.get("/")
def get_cinemas():
    cinemas = list(CinemaModel.select())
    return cinemas


@cinema_route.get("/{cinema_id}")
def get_cinema(cinema_id: int):
    try:
        cinema = CinemaModel.get(CinemaModel.id == cinema_id)
        return cinema
    except CinemaModel.DoesNotExist:
        raise HTTPException(404, "Cinema not found")

@cinema_route.post("/")
def create_cinema(cinema: Cinema = Body(...)):
    CinemaModel.create(name=cinema.name, address=cinema.address, theatersCount=cinema.theatersCount)
    return cinema

@cinema_route.put("/{cinema_id}")
def update_cinema(cinema_id: int, cinema_data: dict):
    try:
        cinema = CinemaModel.get(CinemaModel.id == cinema_id)
        cinema.name = cinema_data.get("name", cinema.name)
        cinema.address = cinema_data.get("address", cinema.address)
        cinema.theatersCount = cinema_data.get("theatersCount", cinema.theatersCount)
        cinema.save()
        return cinema
    except CinemaModel.DoesNotExist:
        raise HTTPException(404, "Cinema not found")

@cinema_route.delete("/{cinema_id}")
def delete_cinema(cinema_id: int):
    try:
        cinema = CinemaModel.get(CinemaModel.id == cinema_id)
        cinema.delete_instance()
        return {"detail": "Cinema deleted successfully"}
    except CinemaModel.DoesNotExist:
        raise HTTPException(404, "Cinema not found")
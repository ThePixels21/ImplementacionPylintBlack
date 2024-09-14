from fastapi import APIRouter, Body, HTTPException
from models.theater import Theater
from database import TheaterModel
from peewee import DoesNotExist

theater_route = APIRouter()

@theater_route.get("/")
def get_theaters():
    theaters = list(TheaterModel.select())
    return theaters

@theater_route.get("/{theater_id}")
def get_theater(theater_id: int):
    try:
        theater = TheaterModel.get(TheaterModel.id == theater_id)
        return theater
    except DoesNotExist:
        raise HTTPException(404, "Theater not found")

@theater_route.post("/")
def create_theater(theater: Theater = Body(...)):
    TheaterModel.create(
        theaterNumber=theater.theaterNumber,
        peopleInside=theater.peopleInside,
        playing=theater.playing,
        capacity=theater.capacity
    )
    return theater

@theater_route.put("/{theater_id}")
def update_theater(theater_id: int, theater_data: dict):
    try:
        theater = TheaterModel.get(TheaterModel.id == theater_id)
        theater.theaterNumber = theater_data.get("theaterNumber", theater.theaterNumber)
        theater.peopleInside = theater_data.get("peopleInside", theater.peopleInside)
        theater.playing = theater_data.get("playing", theater.playing)
        theater.capacity = theater_data.get("capacity", theater.capacity)
        theater.save()
        return theater
    except DoesNotExist:
        raise HTTPException(404, "Theater not found")

@theater_route.delete("/{theater_id}")
def delete_theater(theater_id: int):
    try:
        theater = TheaterModel.get(TheaterModel.id == theater_id)
        theater.delete_instance()
        return {"detail": "Theater deleted successfully"}
    except DoesNotExist:
        raise HTTPException(404, "Theater not found")

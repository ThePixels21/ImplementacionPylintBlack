from fastapi import APIRouter, Body, HTTPException
from models.snack import Snack
from database import SnackModel
from peewee import DoesNotExist

snack_route = APIRouter()

@snack_route.get("/")
def get_snacks():
    snacks = list(SnackModel.select())
    return snacks

@snack_route.get("/{snack_id}")
def get_snack(snack_id: int):
    try:
        snack = SnackModel.get(SnackModel.id == snack_id)
        return snack
    except DoesNotExist:
        raise HTTPException(404, "Snack not found")

@snack_route.post("/")
def create_snack(snack: Snack = Body(...)):
    SnackModel.create(
        name=snack.name,
        description=snack.description,
        type=snack.type,
        price=snack.price
    )
    return snack

@snack_route.put("/{snack_id}")
def update_snack(snack_id: int, snack_data: dict):
    try:
        snack = SnackModel.get(SnackModel.id == snack_id)
        snack.name = snack_data.get("name", snack.name)
        snack.description = snack_data.get("description", snack.description)
        snack.type = snack_data.get("type", snack.type)
        snack.price = snack_data.get("price", snack.price)
        snack.save()
        return snack
    except DoesNotExist:
        raise HTTPException(404, "Snack not found")

@snack_route.delete("/{snack_id}")
def delete_snack(snack_id: int):
    try:
        snack = SnackModel.get(SnackModel.id == snack_id)
        snack.delete_instance()
        return {"detail": "Snack deleted successfully"}
    except DoesNotExist:
        raise HTTPException(404, "Snack not found")
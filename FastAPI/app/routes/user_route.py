from fastapi import APIRouter, Body, HTTPException
from models.user import User
from database import UserModel

user_route = APIRouter()


@user_route.get("/")
def get_users():
    users = list(UserModel.select())
    return users


@user_route.get("/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@user_route.post("/")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user


@user_route.put("/{user_id}")
def update_user(user_id: int, user_data: dict):
    try:
        user = UserModel.get(UserModel.id == user_id)
        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.password = user_data.get("password", user.password)
        user.save()
        return user
    except UserModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        user.delete_instance()
        return {"detail": "User deleted successfully"}
    except UserModel.DoesNotExist:
        raise HTTPException(404, "User not found")

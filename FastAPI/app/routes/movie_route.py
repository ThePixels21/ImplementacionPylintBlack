from fastapi import APIRouter, Body, HTTPException
from models.movie import Movie
from database import MovieModel
from peewee import DoesNotExist

movie_route = APIRouter()

@movie_route.get("/")
def get_movies():
    movies = list(MovieModel.select())
    return movies

@movie_route.get("/{movie_id}")
def get_movie(movie_id: int):
    try:
        movie = MovieModel.get(MovieModel.id == movie_id)
        return movie
    except DoesNotExist:
        raise HTTPException(404, "Movie not found")

@movie_route.post("/")
def create_movie(movie: Movie = Body(...)):
    MovieModel.create(
        name=movie.name,
        description=movie.description,
        actors=movie.actors,
        releaseDate=movie.releaseDate
    )
    return movie

@movie_route.put("/{movie_id}")
def update_movie(movie_id: int, movie_data: dict):
    try:
        movie = MovieModel.get(MovieModel.id == movie_id)
        movie.name = movie_data.get("name", movie.name)
        movie.description = movie_data.get("description", movie.description)
        movie.actors = movie_data.get("actors", movie.actors)
        movie.releaseDate = movie_data.get("releaseDate", movie.releaseDate)
        movie.save()
        return movie
    except DoesNotExist:
        raise HTTPException(404, "Movie not found")

@movie_route.delete("/{movie_id}")
def delete_movie(movie_id: int):
    try:
        movie = MovieModel.get(MovieModel.id == movie_id)
        movie.delete_instance()
        return {"detail": "Movie deleted successfully"}
    except DoesNotExist:
        raise HTTPException(404, "Movie not found")
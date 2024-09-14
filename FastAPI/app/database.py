from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class CinemaModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    theatersCount = IntegerField()

    class Meta:
        database = database
        table_name = "cinemas"

class MovieModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    actors = CharField(max_length=200)
    releaseDate = DateTimeField()

    class Meta:
        database = database
        table_name = "movies"

class SnackModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    type = CharField(max_length=50)
    price = FloatField()

    class Meta:
        database = database
        table_name = "snacks"

class TheaterModel(Model):
    id = AutoField(primary_key=True)
    theaterNumber = IntegerField()
    peopleInside = IntegerField()
    playing = CharField(max_length=50)
    capacity = IntegerField()

    class Meta:
        database = database
        table_name = "theaters"
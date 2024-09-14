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


class ProjectModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)
    init_date = DateField()
    finish_date = DateField()

    class Meta:
        database = database
        table_name = "proyects"

class EmployeeModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=12)
    post = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "employee"

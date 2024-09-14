from fastapi import APIRouter, Body
from FastAPI.app.models.project import Proyect

from database import ProjectModel  

project_route = APIRouter()  

@project_route.get("/")
def get_all_projects():  
    try:
        projects = list(ProjectModel.select())  
        return projects
    except Exception as e:
        print(e)
        return {"error": str(e)}

@project_route.get("/{projectId}")  
def get_project(projectId: int):  
    try:
        project = ProjectModel.get(ProjectModel.id == projectId)  
        return project
    except Exception as e:
        print(e)
        return {"error": str(e)}

@project_route.post("/")
def create_project(project: Proyect = Body(...)):  
    try:
        ProjectModel.create(
            name=project.name, 
            description=project.description, 
            init_date=project.init_date, 
            finish_date=project.finish_date
        )
        return project
    except Exception as e:
        print(e)
        return {"error": str(e)}

@project_route.put("/{projectId}")
def update_project(projectId: int, project: Proyect = Body(...)):  
    try:
        existing_project = ProjectModel.get(ProjectModel.id == projectId)  

        if existing_project is None:
            return "The project doesn't exist"
        else:
            existing_project.name = project.name
            existing_project.description = project.description
            existing_project.init_date = project.init_date
            existing_project.finish_date = project.finish_date

            existing_project.save()
            return "Project updated successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}

@project_route.delete("/{projectId}")
def delete_project(projectId: int):  
    try:
        project = ProjectModel.get(ProjectModel.id == projectId)  
        if project is None:
            return "The project doesn't exist"
        else: 
            project.delete_instance()
            return "Project deleted successfully"
    except Exception as e:
        print(e)
        return {"error": str(e)}


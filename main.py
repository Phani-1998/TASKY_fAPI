from beanie import init_beanie
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import motor
import uvicorn
from src.core.config import settings
from src.models.employeeModel import UserModel
from src.routes import employeeRoutes
from src.routes.employeeRoutes import employee_router
from src.core.db import init_db


# Initialize FastAPI application
def include_router(app):
    app.include_router(employee_router, prefix="/employees")  # Set prefix for employee routes
    # Add more routers as needed
    # e.g., app.include_router(auth_router, prefix="/auth")

def start_application():
    app=FastAPI(title="Taskey API", version="1.0.0")
    include_router(app)
    app.mount("/resources", StaticFiles(directory="resources", html=True), name="site")
    return app

app = start_application()

#Initialize the database on startup
@app.on_event("startup")
async def on_startup():
    await init_db()





    
    
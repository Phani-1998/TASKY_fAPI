import motor
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.models.employeeModel import UserModel
from src.core.config import settings


async def init_db():
     client = AsyncIOMotorClient(settings.MONGO_URI)
     database = client[settings.DATABASE_NAME]
     await init_beanie(database, document_models=[UserModel])


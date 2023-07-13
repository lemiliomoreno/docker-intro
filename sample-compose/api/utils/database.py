import os

from motor.motor_asyncio import AsyncIOMotorClient


MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")


async def get_db():
    mongodb_uri = f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@db:27017"
    print(mongodb_uri)
    client = AsyncIOMotorClient(mongodb_uri)
    return client.academia

from motor.motor_asyncio import AsyncIOMotorClient


async def get_db():
    client = AsyncIOMotorClient("mongodb://academia:academia@172.17.0.2:27017")
    return client.academia

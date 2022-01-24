"""
MongoDB
"""
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import MONGO_URL, MONGO_MAX_CONNECTIONS, MONGO_MIN_CONNECTIONS


class Database:
    """
    DATABASE
    """
    client: AsyncIOMotorClient = None


db = Database()


async def get_database() -> AsyncIOMotorClient:
    """
    Get Database
    :return:
    """
    return db.client


async def connect():
    """
    Connect to MONGO DB
    """
    db.client = AsyncIOMotorClient(str(MONGO_URL),
                                   maxPoolSize=MONGO_MAX_CONNECTIONS,
                                   minPoolSize=MONGO_MIN_CONNECTIONS)
    print(f"Connected to mongo at {MONGO_URL}")


async def close():
    """
    Close MongoDB Connection
    """
    db.client.close()
    print("Closed connection with MongoDB")

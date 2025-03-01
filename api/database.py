from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def get_database(collection_name: str):
    try:
        MONGODB_URL = os.getenv("MONGODB_URL")
        client = AsyncIOMotorClient(MONGODB_URL)
        db = client.get_database("optionsTrading")
        collection = db.get_collection(collection_name)
        return collection
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        raise HTTPException(status_code=500, detail="Database connection failed")
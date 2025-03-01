from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .routes import auth
import os
import platform
import asyncio
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())
# Load environment variables
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection

# db = client.optionsTrading

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


# Include routers
app.include_router(auth.router, prefix="/api/auth")

# @app.middleware("http")
# async def add_db_to_request(request, call_next):
#     request.state.db = db
#     response = await call_next(request)
#     return response

# async def init_db():
#     try:
#         existing_collections = await db.list_collection_names()
#         if "OptionsTrading" not in existing_collections:
#             await db.create_collection("traders")
#             print("Created OptionsTrading collection")
#     except Exception as e:
#         print(f"Error creating collection: {str(e)}")

# Run the initialization
# asyncio.create_task(init_db())
# loop = asyncio.new_event_loop()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB"}

# Example endpoint to get items
@app.get("/items")
async def get_items():
    try:
        # Get count of traders collection
        trader_collection = await get_database("traders")
        count = await trader_collection.count_documents({})
        print(count)
        # Or get all traders
        return {"total_traders": count}
        # return {"message": "Hello World"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Example endpoint to create an item
@app.post("/items")
async def create_item(item: dict):
    try:
        global traders
        result = await traders.insert_one(item)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

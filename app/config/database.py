from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import DESCENDING
from app.models.summary_model import SummaryInDB
from datetime import datetime
from typing import Optional, List
import os


MONGO_URI = os.getenv("MONGO_URI") # Update with your MongoDB connection string

client = AsyncIOMotorClient(MONGO_URI)
if(client):
    print("Connected to MongoDB")
database = client.news_summary
summaries_collection = database.get_collection("summaries")

async def add_summary(category: str, summary: str):
    # summary_data = SummaryInDB(
    #     category=category,
    #     summary=summary,
    #     timestamp=datetime.utcnow()
    # )
    document = {
        "category": category,
        "summary": summary,
        "timestamp": datetime.utcnow()  # Add timestamp if needed
    }
    result = await summaries_collection.insert_one(document)
    return result

async def get_summaries(category: str) -> List[SummaryInDB]:
    documents = await summaries_collection.find({"category": category}).to_list(length=None)  # Adjust length as needed
    summaries = []
    for document in documents:
        document["_id"] = str(document['_id']) # Convert ObjectId to string
        document["timestamp"] = str(document["timestamp"].isoformat())
        summaries.append(SummaryInDB(**document))
    
    return summaries

async def delete_all_summaries():
    result = await summaries_collection.delete_many({})
    return result.deleted_count

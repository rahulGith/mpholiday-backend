import os
from dotenv import load_dotenv

load_dotenv()

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "mp_travel")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

packages = [
    {
        "title": "Ujjain Mahakal Darshan",
        "location": "Ujjain",
        "price": 4999,
        "duration": "2 Days / 1 Night",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41",
        "featured": True,
        "description": "Visit the sacred Mahakaleshwar Jyotirlinga temple."
    },
    {
        "title": "Khajuraho Heritage Tour",
        "location": "Khajuraho",
        "price": 8999,
        "duration": "3 Days / 2 Nights",
        "image": "https://images.unsplash.com/photo-1589881133595-a3c085cb731d",
        "featured": True,
        "description": "Explore the world-famous Khajuraho temples."
    },
    {
        "title": "Pachmarhi Hill Retreat",
        "location": "Pachmarhi",
        "price": 7499,
        "duration": "3 Days / 2 Nights",
        "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "featured": False,
        "description": "Relax in the queen of Satpura hills."
    },
]

async def seed():
    await db.packages.delete_many({})
    await db.packages.insert_many(packages)
    print("✅ Database seeded")

if __name__ == "__main__":
    asyncio.run(seed())
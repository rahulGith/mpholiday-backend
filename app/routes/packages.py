from fastapi import APIRouter
from app.database import db

router = APIRouter()


@router.get("/packages")
async def get_packages():
    packages = await db.packages.find().to_list(100)

    # Convert ObjectId to string
    for package in packages:
        package["_id"] = str(package["_id"])

    return packages

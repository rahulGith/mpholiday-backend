from fastapi import APIRouter
from app.database import db
from app.models import Inquiry

router = APIRouter()


@router.post("/inquiry")
async def create_inquiry(inquiry: Inquiry):
    result = await db.inquiries.insert_one(inquiry.dict())
    return {"success": True, "id": str(result.inserted_id)}

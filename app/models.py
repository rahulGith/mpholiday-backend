from pydantic import BaseModel, EmailStr
from typing import List


class Itinerary(BaseModel):
    day: int
    title: str


class Package(BaseModel):
    title: str
    location: str
    price: int
    duration: str
    image: str
    itinerary: List[Itinerary]


class Inquiry(BaseModel):
    name: str
    email: EmailStr
    phone: str
    message: str

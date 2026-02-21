from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import packages, inquiry

app = FastAPI()

# CORS (temporary open, will restrict later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mpholiday-frontend.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routes
app.include_router(packages.router)
app.include_router(inquiry.router)


@app.get("/")
async def health_check():
    return {"status": "MP Travel API Running"}

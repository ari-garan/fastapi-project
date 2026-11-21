from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.api.v1.router import api_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {"message": "FastAPI application is running"}
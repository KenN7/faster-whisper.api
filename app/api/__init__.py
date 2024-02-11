# File: whisper.api/app/api/__init__.py

from fastapi import APIRouter
from .endpoints import users, transcribe, transcribe_fast

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(transcribe.router, prefix="/transcribe", tags=["transcribe"])
api_router.include_router(transcribe_fast.router, prefix="/transcribe_fast", tags=["transcribe_fast"])

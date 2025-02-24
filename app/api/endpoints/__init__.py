# File: whisper.api/app/api/endpoints/__init__.py

from fastapi import APIRouter

from . import users, transcribe, transcribe_fast

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(transcribe.router, prefix="/transcribe", tags=["transcribe"])
router.include_router(transcribe_fast.router, prefix="/transcribe_fast", tags=["transcribe_fast"])

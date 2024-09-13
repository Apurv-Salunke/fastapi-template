from __future__ import annotations

from fastapi import APIRouter

from .users import user_router

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users")
__all__ = ["api_router"]

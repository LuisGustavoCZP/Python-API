from fastapi import APIRouter, Cookie
from .items import router as itemRouter

router = APIRouter(
    prefix="/api",
    tags=["api"]
)

router.include_router(itemRouter)
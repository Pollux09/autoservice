from fastapi import APIRouter

from .index import router as index_router
from .auth import router as auth_router


router = APIRouter()

router.include_router(
    auth_router
)

router.include_router(
    index_router
)


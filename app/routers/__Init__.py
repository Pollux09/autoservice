from fastapi import APIRouter

from .index import router as index_router
from .auth import router as auth_router
from .clients import router as clients_router
from .warehouse import router as warehouse_router
from .orders import router as orders_router


router = APIRouter()

router.include_router(
    auth_router
)

router.include_router(
    index_router
)

router.include_router(
    clients_router
)

router.include_router(
    warehouse_router
)

router.include_router(
    orders_router
)
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from core.database import db_helper
from core.config import settings
from routers import router as api_router
from core.logger import logger


templates = Jinja2Templates(directory="app/templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    logger.info('FastAPI is starting up')
    yield
    # shutdown
    await db_helper.dispose()
    logger.info('FastAPI is disconnected')


app = FastAPI(title='autoservice', lifespan=lifespan)


# CORS
origins = [
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


# INCLUDE ROUTERS
app.include_router(
    api_router,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.RELOAD)

from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Request

from core.database import db_helper


SessionDep = Annotated[AsyncSession, Depends(db_helper.session_getter)]


def get_access_token(request: Request) -> str | None:
    access_token = request.cookies.get("access_token")
    return access_token


TokenDep = Annotated[str, Depends(get_access_token)]
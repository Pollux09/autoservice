from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.user import get_user_by_email
from app.schemas.user import LoginAuthData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate(session: AsyncSession, auth_data: LoginAuthData):
    user = await get_user_by_email(session=session, email=auth_data.email)
    if not user:
        return False
    if not verify_password(auth_data.password, user.password):
        return False
    return user

from uuid import UUID
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from models import User

async def create_user(
    session: AsyncSession,
    email: str,
    fullname: str,
    phone: str,
    password: str,
    avatar_url: str = '',
    role: str = 'client'
) -> User:
    user = User(
        email=email,
        fullname=fullname,
        phone=phone,
        password=password,
        avatar_url=avatar_url,
        role=role
    )
    session.add(user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise ValueError("User already exists")
    await session.refresh(user)
    return user

async def get_user_by_id(session: AsyncSession, user_id: UUID) -> User:
    result = await session.execute(select(User).filter_by(id=user_id))
    return result.scalar_one_or_none()

async def get_user_by_email(session: AsyncSession, email: str) -> User:
    result = await session.execute(select(User).filter_by(email=email))
    return result.scalar_one_or_none()

async def get_all_users(session: AsyncSession) -> List[User]:
    result = await session.execute(select(User))
    return result.scalars().all()

async def update_user(session: AsyncSession, user_id: UUID, update_data: dict) -> User:
    user = await get_user_by_id(session, user_id)
    if user is None:
        raise ValueError("User not found")
    for key, value in update_data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise ValueError("Update failed, possibly due to duplicate email")
    await session.refresh(user)
    return user

async def delete_user(session: AsyncSession, user_id: UUID) -> bool:
    user = await get_user_by_id(session, user_id)
    if user is None:
        return False
    await session.delete(user)
    await session.commit()
    return True
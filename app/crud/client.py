from uuid import uuid4
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from models import Client

async def create_client(
    session: AsyncSession,
    email: str,
    fullname: str,
    phone: str,
    car: str
) -> Client:
    client = Client(
        id=uuid4(),
        email=email,
        fullname=fullname,
        phone=phone,
        car=car,
        created_at=datetime.utcnow()
    )
    session.add(client)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise ValueError("Клиент с таким email уже существует")
    await session.refresh(client)
    return client



async def get_clients(session: AsyncSession):
    result = await session.execute(select(Client))
    clients = result.scalars().all()
    return clients
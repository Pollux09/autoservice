from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models import SparePart  # Импортируй модель
from datetime import datetime
import uuid

async def create_spare_part(
    session: AsyncSession,
    title: str,
    price: str,
    category: str,
    count: int
) -> SparePart:
    part = SparePart(
        id=uuid.uuid4(),
        title=title,
        price=price,
        category=category,
        count=count,
        created_at=datetime.utcnow()
    )

    session.add(part)

    try:
        await session.commit()
        await session.refresh(part)
        return part
    except IntegrityError:
        await session.rollback()
        raise ValueError("Не удалось создать запчасть — возможен конфликт данных")
    
    
async def get_spare_parts(session: AsyncSession):
    result = await session.execute(select(SparePart))
    parts = result.scalars().all()
    return parts
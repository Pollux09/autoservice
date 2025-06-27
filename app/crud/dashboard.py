from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from models.order import Order


async def get_active_orders_count(
    session: AsyncSession,
) -> int:
    try:
        smtp = select(Order)
        data = await session.execute(smtp)
        result = data.scalars().all()
        return len(result)
    except IntegrityError as e:
        await session.rollback()
        print(e)
        raise ValueError("Не удалось получить количество активных заказов")

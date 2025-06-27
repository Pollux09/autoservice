from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models import Order
from datetime import datetime
import uuid

async def create_order(
    session: AsyncSession,
    car: str,
    description: str,
    price: int
) -> Order:
    order = Order(
        id=uuid.uuid4(),
        car=car,
        description=description,
        status="В ожидании",
        price=price,
        created_at=datetime.utcnow()
    )

    session.add(order)

    try:
        await session.commit()
        await session.refresh(order)
        return order
    except IntegrityError as e:
        await session.rollback()
        print(e)
        raise ValueError("Не удалось создать заказ")
    
    
async def get_orders(session: AsyncSession):
    result = await session.execute(select(Order))
    orders = result.scalars().all()
    return orders
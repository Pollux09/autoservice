from datetime import datetime
from uuid import uuid4

from sqlalchemy import ForeignKey, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    car_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('cars.id'))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    status: Mapped[str] = mapped_column(String(50), default='new')
    description: Mapped[str] = mapped_column(Text, nullable=True)

    car = relationship("Car", back_populates="orders")
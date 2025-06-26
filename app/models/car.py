from uuid import uuid4

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    brand: Mapped[str] = mapped_column(String(255), nullable=False)
    model: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    vin: Mapped[str] = mapped_column(String(17), unique=True, nullable=False)
    owner_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('users.id'))

    owner = relationship("User", back_populates="cars")
    orders = relationship("Order", back_populates="car")
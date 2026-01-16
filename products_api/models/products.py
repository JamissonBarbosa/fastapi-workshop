from sqlalchemy import Mapped, mapped_column
from sqlalchemy import Numeric, Text, func
from datetime import datetime 
from decimal import Decimal
from typing import Optional


from products_api.models import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)


    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(), server_default=func.now(),
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
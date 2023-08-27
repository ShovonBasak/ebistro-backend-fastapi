from sqlalchemy import Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class DomainEntityBase(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
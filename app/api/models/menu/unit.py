from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.api.models.base.domain_entity import DomainEntityBase


class Unit(DomainEntityBase):
    __tablename__ = 'units'

    name: Mapped[str] = mapped_column(String(50))
    abbreviation: Mapped[str] = mapped_column(String(10))
    description: Mapped[Optional[str]] = mapped_column(String(255))

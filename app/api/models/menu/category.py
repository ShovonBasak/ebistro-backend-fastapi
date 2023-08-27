from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.api.models.base.domain_entity import DomainEntityBase


class Category(DomainEntityBase):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255))

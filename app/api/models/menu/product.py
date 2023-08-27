from typing import Optional

from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.api.models.base.organization_domain_entity import OrganizationDomainEntityBase

from app.api.models import Category, Unit


class Product(OrganizationDomainEntityBase):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id'))
    unit_id: Mapped[int] = mapped_column(Integer, ForeignKey('unit.id'))

    category: Mapped['Category'] = relationship('Category', back_populates='products')
    unit: Mapped['Unit'] = relationship('Unit', back_populates='products')


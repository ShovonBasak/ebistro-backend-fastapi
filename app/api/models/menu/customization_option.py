from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.api.models import OrganizationDomainEntityBase
from app.api.models.menu import Product


class CustomizationOption(OrganizationDomainEntityBase):
    __tablename__ = "customization_options"

    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    name: Mapped[str] = mapped_column(String(100))
    value: Mapped[str] = mapped_column(String(255))

    product: Mapped['Product'] = relationship("Product", back_populates='customization_options')

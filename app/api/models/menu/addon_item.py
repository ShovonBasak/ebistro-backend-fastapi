from sqlalchemy import Integer, ForeignKey, String, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.api.models import OrganizationDomainEntityBase
from app.api.models.menu import Product


class AddonItem(OrganizationDomainEntityBase):
    __tablename__ = "addon_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    cart_item_id: Mapped[int] = mapped_column(Integer, ForeignKey("cart_items.id"))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"))
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)

    product: Mapped['Product'] = relationship("Product", back_populates="addon_items")
from sqlalchemy import Column, String

from app.api.models.base.domain_entity import DomainEntityBase


class Organization(DomainEntityBase):
    __tablename__ = 'organizations'

    name = Column(String, index=True, nullable=False)
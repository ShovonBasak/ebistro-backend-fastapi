from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from app.api.models.base.domain_entity import DomainEntityBase

from app.api.models import Organization


class OrganizationDomainEntityBase(DomainEntityBase):
    __abstract__ = True

    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization: Mapped['Organization'] = relationship('Organization')
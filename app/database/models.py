from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.base import Base


class DomainBase(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)


class Entity(DomainBase):
    __tablename__ = 'entities'

    name = Column(String, index=True, nullable=False)


class DomainEntityBase(DomainBase):
    __abstract__ = True

    entity_id = Column(Integer, ForeignKey("entities.id"))

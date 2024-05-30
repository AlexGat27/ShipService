from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Danger(Base):
    __tablename__ = "dangers"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    danger_for_system = relationship("Danger4System", back_populates='danger', uselist=False, cascade="all,delete")

class Danger4System(Base):
    __tablename__ = "danger_for_system"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ship_system_id = Column(Integer, ForeignKey("ship_systems.id", ondelete='CASCADE'))
    danger_id = Column(Integer, ForeignKey("dangers.id", ondelete='CASCADE'))

    ship_system = relationship("ShipSystem", back_populates='danger_for_system')
    danger = relationship("Danger", back_populates='danger_for_system', uselist=False)
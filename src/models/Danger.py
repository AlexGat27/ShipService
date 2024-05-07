from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Danger(Base):
    __tablename__ = "danger"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    danger_for_system = relationship("Danger4System", back_populates='danger', uselist=False)

class Danger4System(Base):
    __tablename__ = "danger_for_system"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ship_system_id = Column(Integer, ForeignKey("ship_system.id"))
    danger_id = Column(Integer, ForeignKey("danger.id"))

    ship_system = relationship("ShipSystem", back_populates='danger_for_system')
    danger = relationship("Danger", back_populates='danger_for_system', uselist=False)
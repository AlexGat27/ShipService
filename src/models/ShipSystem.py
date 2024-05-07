from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class ShipSystem(Base):
    __tablename__ = "ship_system"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ship_id = Column(Integer, ForeignKey("ship.id"))

    ship = relationship("Ship", back_populates="ship_system")
    security_indicator = relationship("SecurityIndicator", back_populates="ship_system")
    equipment = relationship("Equipment", back_populates="ship_system")
    danger_for_system = relationship("Danger4System", back_populates="ship_system")
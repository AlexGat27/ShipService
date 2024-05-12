from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    ship_system = relationship("ShipAndSystem", back_populates="ship")

class ShipSystem(Base):
    __tablename__ = "ship_systems"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)

    ship = relationship("ShipAndSystem", back_populates="ship_system")
    security_indicator = relationship("SystemAndIndicator", back_populates="ship_system")
    equipment = relationship("Equipment", back_populates="ship_system")
    danger_for_system = relationship("Danger4System", back_populates="ship_system")

class ShipAndSystem(Base):
    __tablename__ = "ship_and_systems"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ship_id = Column(Integer, ForeignKey("ships.id"))
    ship_system_id = Column(Integer, ForeignKey("ship_systems.id"))

    ship = relationship("Ship", back_populates="ship_system")
    ship_system = relationship("ShipSystem", back_populates="ship")
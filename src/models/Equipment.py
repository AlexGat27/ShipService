from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ship_system_id = Column(Integer, ForeignKey("ship_system.id"))

    ship_system = relationship("ShipSystem", back_populates='equipment')
    vulnerability = relationship("Vulnerability", back_populates='equipment')
    protection = relationship("Protection", back_populates='equipment')
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Ship(Base):
    __tablename__ = "ship"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    ship_system = relationship("ShipSystem", back_populates="ship")
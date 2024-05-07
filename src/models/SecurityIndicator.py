from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class SecurityIndicator(Base):
    __tablename__ = "security_indicator"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    ship_system_id = Column(Integer, ForeignKey("ship_system.id"))

    ship_system = relationship("ShipSystem", back_populates='security_indicator')
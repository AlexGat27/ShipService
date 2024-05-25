from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class SecurityIndicator(Base):
    __tablename__ = "security_indicators"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    ship_system = relationship("SystemAndIndicator", back_populates='security_indicator')

class SystemAndIndicator(Base):
    __tablename__ = "system_and_indicators"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    ship_system_id = Column(Integer, ForeignKey("ship_systems.id", ondelete='CASCADE'))
    security_indicator_id = Column(Integer, ForeignKey("security_indicators.id", ondelete='CASCADE'))

    ship_system = relationship("ShipSystem", back_populates='security_indicator')
    security_indicator = relationship("SecurityIndicator", back_populates='ship_system')
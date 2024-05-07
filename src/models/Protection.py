from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .db import Base

class Protection(Base):
    __tablename__ = "protection"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))

    equipment = relationship("Equipment", back_populates="protection")
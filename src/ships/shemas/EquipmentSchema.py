from pydantic import BaseModel

class EquipmentSchema(BaseModel):
    title: str
    description: str
    type: str

class SystemAndEquipmentSchema(BaseModel):
    ship_system: str
    equipment: str
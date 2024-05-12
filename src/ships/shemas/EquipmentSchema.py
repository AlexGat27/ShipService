from pydantic import BaseModel

class EquipmentSchema(BaseModel):
    title: str
    description: str
    type: str
    ship_system: str
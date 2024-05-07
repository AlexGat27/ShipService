from pydantic import BaseModel

class EquipmentSchema(BaseModel):
    name: str
    description: str
    type: str
    ship_system: str
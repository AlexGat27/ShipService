from pydantic import BaseModel

class ShipSchema(BaseModel):
    name: str
    description: str

class ShipSystemSchema(BaseModel):
    name: str
    description: str
    type: str

class ShipAndSystemSchema(BaseModel):
    ship: str
    ship_system: str
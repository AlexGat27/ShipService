from pydantic import BaseModel

class ShipSchema(BaseModel):
    title: str
    description: str

class ShipSystemSchema(BaseModel):
    title: str
    description: str
    type: str
    category: int
    document: str

class ShipAndSystemSchema(BaseModel):
    ship: str
    ship_system: str
from pydantic import BaseModel

class ShipSchema(BaseModel):
    name: str
    description: str
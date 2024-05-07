from typing import Union
from pydantic import BaseModel

class ShipSystemSchema(BaseModel):
    name: str
    description: str
    type: str
    ship: str | int
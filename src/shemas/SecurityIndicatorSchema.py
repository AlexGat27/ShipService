from pydantic import BaseModel

class SecurityIndicatorSchema(BaseModel):
    name: str
    description: str
    ship_system: str | int
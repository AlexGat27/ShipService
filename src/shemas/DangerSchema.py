from pydantic import BaseModel

class DangerSchema(BaseModel):
    name: str
    description: str
    ship_system: str | None
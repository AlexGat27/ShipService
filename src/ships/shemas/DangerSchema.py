from pydantic import BaseModel

class DangerSchema(BaseModel):
    title: str
    description: str
    ship_system: str | None
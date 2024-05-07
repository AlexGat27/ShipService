from pydantic import BaseModel

class ProtectionSchema(BaseModel):
    name: str
    description: str
    equipment: str
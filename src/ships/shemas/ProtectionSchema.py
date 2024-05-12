from pydantic import BaseModel

class ProtectionSchema(BaseModel):
    title: str
    description: str
    equipment: str
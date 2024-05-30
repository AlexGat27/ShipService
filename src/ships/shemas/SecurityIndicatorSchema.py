from pydantic import BaseModel

class SecurityIndicatorSchema(BaseModel):
    title: str
    description: str

class SystemAndIndicatorSchema(BaseModel):
    ship_system: str
    security_indicator: str
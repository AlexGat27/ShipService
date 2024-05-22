from pydantic import BaseModel
from . import ShipSchema, SecurityIndicatorSchema, DangerSchema, ShipSystemSchema, EquipmentSchema, ProtectionSchema, VulnerabilitySchema

class ShipModelSchema(BaseModel):

    class SystemShipModelSchema(BaseModel):

        class EquipmentModelSchema(BaseModel):
            equipment: EquipmentSchema
            protections: list[ProtectionSchema]
            vulnerabilities: list[VulnerabilitySchema]

        system_ship: ShipSystemSchema
        security_indicators: list[SecurityIndicatorSchema]
        dangers: list[DangerSchema]
        equipments: list[EquipmentModelSchema]


    ship: ShipSchema
    ship_systems: list[SystemShipModelSchema]
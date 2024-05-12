from fastapi import APIRouter, HTTPException
from .shemas import *
from .controllers.CreateModelsController import CreateModelsController

router = APIRouter(
    prefix="/api/v1",
    tags=["Ships"]
)

create_controller = CreateModelsController()

@router.post("/create/ship")
async def create_ship(data: ShipSchema):
    await create_controller.create_ship(data)
    return {"message": "Model created successfully"}

@router.post("/create/ship-system")
async def create_ship_system(data: ShipSystemSchema):
    print(data)
    await create_controller.create_ship_system(data)
    return {"message": "Model created successfully"}

@router.post("/create/equipment")
async def create_equipment(data: EquipmentSchema):
    await create_controller.create_equipment(data)
    return {"message": "Model created successfully"}

@router.post("/create/security-indicator")
async def create_security_indicator(data: SecurityIndicatorSchema):
    await create_controller.create_security_indicator(data)
    return {"message": "Model created successfully"}

@router.post("/create/danger")
async def create_danger(data: DangerSchema):
    await create_controller.create_danger(data)
    return {"message": "Model created successfully"}

@router.post("/create/protection")
async def create_protection(data: ProtectionSchema):
    await create_controller.create_protection(data)
    return {"message": "Model created successfully"}

@router.post("/create/vulnerability")
async def create_vulnerability(data: VulnerabilitySchema):
    await create_controller.create_vulnerability(data)
    return {"message": "Model created successfully"}

@router.post("/create/system-ship-association")
async def create_ship_system_association(data: ShipAndSystemSchema):
    await create_controller.create_ship_system_association(data)
    return {"message": "Model created successfully"}

@router.post("/create/security-sys-association")
async def create_system_indicator_association(data: SystemAndIndicatorSchema):
    await create_controller.create_system_indicator_association(data)
    return {"message": "Model created successfully"}
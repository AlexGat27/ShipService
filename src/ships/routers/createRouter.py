from fastapi import APIRouter, HTTPException
from ..shemas import *
from ..controllers.CreateModelsController import CreateModelsController

router = APIRouter(
    prefix="/api/v1/create",
    tags=["Ships"]
)

create_controller = CreateModelsController()

@router.post("/ship")
async def create_ship(data: ShipSchema):
    if await create_controller.create_ship(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/ship-system")
async def create_ship_system(data: ShipSystemSchema):
    if await create_controller.create_ship_system(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/equipment")
async def create_equipment(data: EquipmentSchema):
    if await create_controller.create_equipment(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/security-indicator")
async def create_security_indicator(data: SecurityIndicatorSchema):
    if await create_controller.create_security_indicator(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/danger")
async def create_danger(data: DangerSchema):
    if await create_controller.create_danger(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/protection")
async def create_protection(data: ProtectionSchema):
    if await create_controller.create_protection(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/vulnerability")
async def create_vulnerability(data: VulnerabilitySchema):
    if await create_controller.create_vulnerability(data):
        return data.title
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/system-ship-association")
async def create_ship_system_association(data: ShipAndSystemSchema):
    if await create_controller.create_ship_system_association(data):
        return {"model1": data.ship, "model2": data.ship_system}
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/security-sys-association")
async def create_system_indicator_association(data: SystemAndIndicatorSchema):
    if await create_controller.create_system_indicator_association(data):
        return {"model1": data.ship, "model2": data.ship_system}
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")

@router.post("/system-equipment-association")
async def create_system_equipment_association(data: SystemAndEquipmentSchema):
    if await create_controller.create_system_equipment_association(data):
        return {"model1": data.ship, "model2": data.ship_system}
    else: raise HTTPException(409, detail="Неудачная запись в базу данных")
from fastapi import APIRouter, HTTPException
from ..models import *
from ..controllers.GetShipController import GetShipController
get_controller = GetShipController()

# Модели

modelRouter = APIRouter(
    prefix="/api/v1/getModel",
    tags=["Ships"]
)

@modelRouter.get("/ships")
async def get_ships():
    return await get_controller.getModels(Ship)

@modelRouter.get("/ship-systems")
async def get_ship_systems():
    return await get_controller.getModels(ShipSystem)

@modelRouter.get("/equipments")
async def get_equipments():
    return await get_controller.getModels(Equipment)

@modelRouter.get("/security-indicators")
async def get_equipments():
    return await get_controller.getModels(SecurityIndicator)

@modelRouter.get("/dangers")
async def get_danger():
    return await get_controller.getModels(Danger)

@modelRouter.get("/protections")
async def get_protection():
    return await get_controller.getModels(Protection)

@modelRouter.get("/vulnerabilities")
async def get_vulnerability():
    return await get_controller.getModels(Vulnerability)



# Ассоциации
associationRouter = APIRouter(
    prefix="/api/v1/getAssociation",
    tags=["Ships"]
)

@associationRouter.get("/ship-systems")
async def get_ship_system_association():
    return await get_controller.get_ship_system_association()

@associationRouter.get("/equipment-systems")
async def get_system_equipment_association():
    return await get_controller.get_system_equipment_association()

@associationRouter.get("/security-systems")
async def get_system_security_association():
    return await get_controller.get_system_security_association()
from fastapi import APIRouter, HTTPException
from ..models import *
from ..controllers.SelectShipController import SelectShipController
select_controller = SelectShipController()

# Модели

selectRouter = APIRouter(
    prefix="/api/v1/selectModel",
    tags=["Ships"]
)

@selectRouter.get("/ship")
async def get_ship_model(ship_name: str):
    print(ship_name)
    return await select_controller.get_ship_model(ship_name)
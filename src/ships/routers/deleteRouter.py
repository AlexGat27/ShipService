from fastapi import APIRouter, HTTPException
from ..models import *
from ..controllers.DeleteModelsController import DeleteModelsController
delete_controller = DeleteModelsController()

# Модели

router = APIRouter(
    prefix="/api/v1/deleteModel",
    tags=["Ships"]
)

@router.delete("")
async def delete_model(id: int, tablename: str):
    status = await delete_controller.delete_model(id, tablename)
    if status == 200:
        return {"message": "Модель успешно удалена"}
    elif status == 404:
        raise HTTPException(404, detail="Ошибка при удалении, модель не найдена")
    elif status == 400: 
        raise HTTPException(400, detail="Ошибка при удалении, проверьте, нет ли зависимых ключей")
    else: 
        raise HTTPException(400, detail="Неизвестная ошибка при удалении")
# from src.controllers.UserFormController import UserFormController

# if __name__ == "__main__":
#     controller = UserFormController()
#     controller.startMenu()

from fastapi import FastAPI
from src.ships.routers.createRouter import router as create_router
from src.ships.routers.getRouter import modelRouter, associationRouter

app = FastAPI(title="ship_app")

app.include_router(create_router)
app.include_router(modelRouter)
app.include_router(associationRouter)


            
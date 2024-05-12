# from src.controllers.UserFormController import UserFormController

# if __name__ == "__main__":
#     controller = UserFormController()
#     controller.startMenu()

from fastapi import FastAPI
from src.ships.router import router as ship_router

app = FastAPI(title="ship_app")

app.include_router(ship_router)


            
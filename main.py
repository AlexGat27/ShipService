from fastapi import FastAPI
from src.ships.routers.createRouter import router as createRouter
from src.ships.routers.getRouter import modelRouter, associationRouter
from src.ships.routers.modelRouter import selectRouter
from src.ships.routers.deleteRouter import router as deleteRouter

app = FastAPI(title="ship_app")

app.include_router(createRouter)
app.include_router(modelRouter)
app.include_router(associationRouter)
app.include_router(selectRouter)
app.include_router(deleteRouter)


            
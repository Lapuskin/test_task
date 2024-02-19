from fastapi import APIRouter

from app.src.controllers import notes_controller
from src.controllers import user_controller


def get_apps_router():
    router = APIRouter(prefix='/api/v1', tags=['api'])
    router.include_router(notes_controller.router)
    router.include_router(user_controller.router)

    return router
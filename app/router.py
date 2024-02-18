from fastapi import APIRouter

from app.src.controllers import notes_controller


def get_apps_router():
    router = APIRouter()
    router.include_router(notes_controller.router)
    return router
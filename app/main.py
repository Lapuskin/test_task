import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.router import get_apps_router
from app.src.config import settings
from app.src.config.db_settings.db_settings import engine, SessionLocal
from app.src.models.notes_model import Base


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_SETTINGS['PROJECT_NAME'],
        debug=settings.PROJECT_SETTINGS['DEBUG'],
        version=settings.PROJECT_SETTINGS['VERSION']
    )
    application.include_router(get_apps_router())

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
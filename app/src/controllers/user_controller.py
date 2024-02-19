from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.src.services.notes_services import UserHandler
from src.config.db_settings.db_settings import get_db
from src.services.auth import get_curr_user
from src.services.base_service import AbstractCRUDHandler

router = APIRouter(prefix='/users', tags=['users'])

user_handler: AbstractCRUDHandler = UserHandler()




@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return user_handler.all(db)


@router.get("/{id}")
def get_note(id: int, db: Session = Depends(get_db)):
    return user_handler.get(id, db)


@router.post("/")
def create_note(data=Body(), db: Session = Depends(get_db)):
    user = user_handler.create(data, db)
    return user


@router.put("/")
def update_note(data=Body(), db: Session = Depends(get_db)):
    user = user_handler.update(data, db)
    if user is None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    else:
        return user


@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)):
    return user_handler.delete(id, db)
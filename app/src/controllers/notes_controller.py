from fastapi import APIRouter, Body, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.src.services.notes_services import NotesHandler
from src.config.db_settings.db_settings import get_db
from src.services.auth import get_curr_user
from src.services.base_service import AbstractCRUDHandler

router = APIRouter(prefix='/notes', tags=['notes'])

notes_handler: AbstractCRUDHandler = NotesHandler()


from fastapi import Depends




@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return notes_handler.all(db)


@router.get("/{id}")
def get_note(id: int, db: Session = Depends(get_db)):
    return notes_handler.get(id, db)


@router.post("/")
def create_note(data=Body(), db: Session = Depends(get_db)):
    note = notes_handler.create(data, db)
    return note


@router.put("/")
def update_note(data=Body(), db: Session = Depends(get_db)):
    note = notes_handler.update(data, db)
    if note is None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    else:
        return note


@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db)):
    return notes_handler.delete(id, db)

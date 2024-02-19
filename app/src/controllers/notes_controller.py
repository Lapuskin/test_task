from fastapi import APIRouter, Body, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.src.services.notes_services import NotesHandler
from src.config.db_settings.db_settings import get_db
from src.controllers.auth import check_auth
from src.services.auth import get_curr_user
from src.services.base_service import AbstractCRUDHandler

router = APIRouter(prefix='/notes', tags=['notes'])

notes_handler: AbstractCRUDHandler = NotesHandler()


from fastapi import Depends


@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return notes_handler.all(db)


@router.get("/{id}")
def get_note(id: int, db: Session = Depends(get_db), user=Depends(get_curr_user)):
    #я помню про DRY, но FastAPI не позволил мне использовать декораторы на роутах(
    note = notes_handler.get(id, db)
    current_user = check_auth(user)
    if note.user_id != current_user["id"]:
        raise HTTPException(status_code=403)
    else:
        return note


@router.post("/")
def create_note(data=Body(), db: Session = Depends(get_db)):
    note = notes_handler.create(data, db)
    return note


@router.put("/")
def update_note(data=Body(), db: Session = Depends(get_db), user=Depends(get_curr_user)):
    note = notes_handler.get(data['id'])
    if note is None:
        return JSONResponse(status_code=404, content={"message": "Заметка не найдена"})
    current_user = check_auth(user)
    if note.user_id != current_user["id"]:
        raise HTTPException(status_code=403)
    else:
        return notes_handler.update(data, db, note)



@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db), user=Depends(get_curr_user)):
    note = notes_handler.get(id, db)
    if note is None:
        return JSONResponse(status_code=404, content={"message": "Заметка не найдена"})
    current_user = check_auth(user)
    if note.user_id != current_user["id"]:
        raise HTTPException(status_code=403)
    else:
        return notes_handler.delete(note.id)

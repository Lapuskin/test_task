from fastapi import APIRouter

from app.src.services.notes_services import NotesHandler

router = APIRouter(prefix='/notes', tags=['notes'])

notes_handler = NotesHandler()


@router.get('/')
def get_all():
    return ''


@router.get("/{id}")
def get_note():
    pass


@router.post("/")
def create_note():
    pass


@router.put("/{id}")
def update_note():
    pass


@router.delete("/{id}")
def delete_note():
    pass

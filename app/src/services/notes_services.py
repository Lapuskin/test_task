from datetime import datetime

from sqlalchemy.orm import Session

from app.src.services.base_service import AbstractCRUDHandler

from src.models.notes_model import Note


class NotesHandler(AbstractCRUDHandler):
    def all(self, db: Session):
        return db.query(Note).all()

    def get(self, id: int, db: Session):
        note = db.query(Note).filter(Note.id == id).first()
        return note

    def create(self, data: dict, db: Session):
        note = Note(
            title=data["title"],
            content=data["content"],
            user_id=data["user_id"]
        )
        db.add(note)
        db.commit()
        db.refresh(note)
        return note

    def update(self, data: dict, db: Session, note: Note):
        note.title = data["title"]
        note.content = data["content"]
        note.user_id = data["user_id"]
        note.updated_at = datetime.now()
        db.commit()
        db.refresh(note)
        return note

    def delete(self, id: int, db: Session):
        try:
            note = db.query(Note).filter(Note.id == id).first()
            db.delete(note)
            db.commit()
            return note
        except:
            return None


    def filter(self, db: Session, **kwargs):
        query = db.query(Note)
        for key, value in kwargs.items():
            query = query.filter(getattr(Note, key) == value)

        notes = query.all()
        return notes


from datetime import datetime

from sqlalchemy.orm import Session

from app.src.services.base_service import AbstractCRUDHandler
from src.services.auth import bcrypt_context
from src.models.notes_model import Note, User


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

    def update(self, data: dict, db: Session):
        note = db.query(Note).filter(Note.id == data["id"]).first()
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


class UserHandler(AbstractCRUDHandler):
    def all(self, db: Session):
        return db.query(User).all()

    def get(self, id: int, db: Session):
        user = db.query(User).filter(User.id == id).first()
        return user

    def create(self, data: dict, db: Session):
        user = User(
            name=data["name"],
            email=data["email"],
            password=bcrypt_context.hash(data["password"])
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, data: dict, db: Session):
        user = db.query(User).filter(User.id == data["id"]).first()
        user.name = data["name"]
        user.email = data["email"]
        db.commit()
        db.refresh(user)
        return user

    def delete(self, id: int, db: Session):
        try:
            user = db.query(User).filter(User.id == id).first()
            db.delete(user)
            db.commit()
            return user
        except:
            return None

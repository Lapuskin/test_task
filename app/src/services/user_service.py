
from sqlalchemy.orm import Session

from app.src.services.base_service import AbstractCRUDHandler
from src.services.auth import bcrypt_context
from src.models.notes_model import User

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

    def update(self, data: dict, db: Session, user: User):
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

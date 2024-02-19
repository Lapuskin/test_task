from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class AbstractCRUDHandler(ABC):
    @abstractmethod
    def all(self, db: Session):
        pass

    @abstractmethod
    def get(self, id: int, db: Session):
        pass

    @abstractmethod
    def create(self, data: dict, db: Session):
        pass

    @abstractmethod
    def update(self, data: dict, db: Session, entity):
        pass

    @abstractmethod
    def delete(self, id: int, db: Session):
        pass

    @abstractmethod
    def filter(self, db: Session, **kwargs):
        pass

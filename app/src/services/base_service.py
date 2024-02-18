from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class AbstractCRUDHandler(ABC):
    def __init__(self, db: Session):
        self.__db = db

    @abstractmethod
    def get(self, **kwargs):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self):
        pass
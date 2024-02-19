from datetime import datetime

from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, default=func.uuid_generate_v4())
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    notes = relationship('Note', back_populates='user')


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, default=func.uuid_generate_v4())
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User', back_populates='notes')
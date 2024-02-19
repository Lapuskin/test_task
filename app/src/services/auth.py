import datetime

from fastapi import HTTPException, Cookie
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status

from src.config.settings import AUTH_SETTINGS
from src.models.notes_model import User

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_access_token(username: str, user_id: int, expires_delta: datetime.timedelta):
    '''Создаем токен здесь, добавляем полезную нагрузку и шифруем секретным ключом'''
    expires = datetime.datetime.utcnow() + expires_delta
    encode = {
        'sub': username,
        'id': user_id,
        'exp': expires
    }

    return jwt.encode(encode, AUTH_SETTINGS['SECRET_KEY'], algorithm=AUTH_SETTINGS['ALGORITHM'])


def authenicate_user(username: str, password: str, db: Session):
    ''''''
    user = db.query(User).filter(User.name == username).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    else:
        return user


async def get_curr_user(jwt_token=Cookie()):
    '''Проверка подлинности запроса. Авторизация.'''
    try:
        payload = jwt.decode(jwt_token, AUTH_SETTINGS['SECRET_KEY'])
        name: str = payload.get('sub')
        id: int = payload.get('id')
        if name is None or id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return {'name': name, 'id': id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

from datetime import timedelta

from fastapi import APIRouter, Depends, Body, HTTPException, Response

from sqlalchemy.orm import Session
from starlette import status

from src.config.db_settings.db_settings import get_db
from src.services.auth import authenicate_user, create_access_token, get_curr_user

router = APIRouter(prefix='/auth', tags=['auth'])


@router.get('/check')
def check_permissions(user=Depends(get_curr_user)):
    if user is None:
        raise HTTPException(status_code=401)
    return user


@router.post("/")
def register(data=Body(), db: Session = Depends(get_db)):
    pass


@router.post("/token")
def login_for_access_token(response: Response, data=Body(), db: Session = Depends(get_db)):
    user = authenicate_user(data['name'], data['password'], db)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)
    token = create_access_token(user.name, user.id, timedelta(minutes=20))
    response.set_cookie(key="jwt_token", value=token, httponly=True)
    response.headers["Authentication-Method"] = "Bearer"
    return {"message": "Logged in successfully"}

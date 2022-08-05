from fastapi import APIRouter, Depends, status
from db import models
from db.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from auth import oauth2

router = APIRouter(tags=['auth'])

@router.post('/token')
def get_token(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    access_token = oauth2.create_access_token(data={'sub':user.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found user')
    elif user.password != request.password:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid password')
    else:
        return {
        'access_token':access_token,
        'type_token':'bearer',
        'userID':user.id,
        'usename':user.username
        }
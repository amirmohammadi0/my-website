from typing import List
from fastapi import APIRouter, Depends
from db import db_user
from db.database import get_db
import schemas
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user',tags=['user'])



@router.post('/creat',response_model=schemas.UserDisplay)
async def create_user(user:schemas.UserBase, db:Session = Depends(get_db)):
    return db_user.creat_user(user,db)


@router.get('/',response_model=List[schemas.UserDisplay])
def get_all_users(db=Depends(get_db)):
    return db_user.get_all_users(db)


@router.get('/{id}',response_model=schemas.UserDisplay)
def get_user(id:int, db=Depends(get_db)):
    return db_user.get_user(id,db)



@router.get('/delete/{id}')
def delete_user(id:int, db=Depends(get_db)):
    return db_user.delete_user(id,db)


@router.post('/update/{id}')
async def update_user(id:int, user:schemas.UserBase, db:Session = Depends(get_db)):
    return db_user.update_user(id, db, user)

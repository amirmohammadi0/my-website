from db import models
from schemas import UserBase
from sqlalchemy.orm import Session
from db._hash import Hash


def creat_user(user:UserBase,db:Session):
    user = models.User(
        username = user.username,
        email = user.email,
        password = Hash.bcrypt(user.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:Session):
    return db.query(models.User).all()


def get_user(id, db:Session):
    return db.query(models.User).filter(models.User.id ==id).first()

def get_user_by_username(username, db:Session):
    return db.query(models.User).filter(models.User.username ==username).first()

def delete_user(id, db:Session):
    user = get_user(id,db)
    db.delete(user)
    db.commit()
    return 'ok'


def update_user(id,db:Session,request:UserBase):
    user = db.query(models.User).filter(models.User.id == id)
    user.update(
        {
            models.User.username:request.username,
            models.User.email:request.email,
            models.User.password:Hash.bcrypt(request.password)
        }
    )
    db.commit()
    return 'ok'
from fastapi import APIRouter, Depends
from db import db_article
from db.database import get_db
import schemas
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user


router = APIRouter(prefix='/article',tags=['article'])


@router.post('/creat',response_model=schemas.ArticleDisplay)
async def create_article(article:schemas.ArticleBase, db:Session = Depends(get_db)):
    return db_article.create_article(db,article)

# @router.get('/{id}',response_model=schemas.ArticleDisplay)
# def get_article(id:int, db=Depends(get_db)):
#     return db_article.get_article(id,db)


@router.get('/{id}')
def get_article(id:int, db=Depends(get_db),current_user:schemas.UserBase=Depends(get_current_user)):
    return {
        'data':db_article.get_article(id,db),
        'current_user':current_user
    }
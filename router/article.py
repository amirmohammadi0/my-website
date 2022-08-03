from fastapi import APIRouter, Depends
from db import db_article
from db.database import get_db
import schemas
from sqlalchemy.orm import Session


router = APIRouter(prefix='/article',tags=['article'])


@router.post('/creat',response_model=schemas.ArticleDisplay)
async def create_article(article:schemas.ArticleBase, db:Session = Depends(get_db)):
    return db_article.create_article(db,article)

@router.get('/{id}',response_model=schemas.ArticleDisplay)
def get_article(id:int, db=Depends(get_db)):
    return db_article.get_article(id,db)
from db import models
from schemas import ArticleBase
from sqlalchemy.orm import Session

def create_article(db:Session, request:ArticleBase):
    article = models.Article(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.user_id,
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(id, db:Session):
    return db.query(models.Article).filter(models.Article.id ==id).first()


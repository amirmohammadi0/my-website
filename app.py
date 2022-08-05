from fastapi import FastAPI
from db.database import Base,engine
from router import user,article
from auth import authentication

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)
app.include_router(authentication.router)

@app.get('/',tags=['index page'])
async def index():
    return {
        'message':'Home Page'
    }

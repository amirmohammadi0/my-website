from typing import List
from pydantic import BaseModel

# will get from client
class UserBase(BaseModel):
    username : str
    email : str
    password : str

# will get from client
class ArticleBase(BaseModel):
    title : str
    content : str
    published : bool
    user_id : int

# show in the User Display 
class Article(BaseModel):
    title : str
    content : str
    published : bool

    class Config:
        orm_mode = True

# show user in request/return
class UserDisplay(BaseModel):
    username : str
    email : str
    items : List[Article] = []

    class Config:
        orm_mode = True

# show creator/user in the Article Display
class User(BaseModel):
    id: int
    username : str

    class Config:
        orm_mode = True

class ArticleDisplay(BaseModel):
    title : str
    content : str
    published : bool
    user: User

    class Config:
        orm_mode = True
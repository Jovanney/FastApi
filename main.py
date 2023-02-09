from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name': 'Jova'}}

@app.get('/blog')
def about(limit: int =10, published: bool = True, sort: Optional[str] = None): #set 10 and True by default
    #only get Limit published blogs
    
    if published:
        return {'data': f'{limit} blogs from the db'}
    else:
        return {'data': f'there are not any published blogs'}
    

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def index(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data': {'1', '2'}}

#Post = Create something

class Blog(BaseModel):  #Model
    title: str
    body: str
    published_at: Optional[bool]
    

@app.post('/blog')
def createBlog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}

#SQLAlchemy's philosophy


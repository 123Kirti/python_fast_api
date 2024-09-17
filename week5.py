from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

#title str, content str, category
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title":"title of post 1","content":"content of post 1","id":1}, {"title":"fav food","content":"i like food","id":2}]



#request get method url: "/"
@app.get("/") #get http method [just a path to execute the code][\ is for the root path, this refers to the path we need to go or visit]
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}


def find_post(id):
    for p in my_posts:
        if p["id"] == int(id):
            return p 

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found"}
    return {"post-details": post}
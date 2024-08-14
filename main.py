from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

#title str, content str, category
class Post(BaseModel):
    title: str
    content: str


#request get method url: "/"
@app.get("/") #get http method [just a path to execute the code][\ is for the root path, this refers to the path we need to go or visit]
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post."}

@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    return {"data":"new post"}
  
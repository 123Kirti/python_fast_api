'''
Objective: Set up and understand FAST API for creating a web-based API.
Tasks:
Install and configure FAST API.
Create basic endpoints for adding and retrieving records.
Test API endpoints using tools like Postman.

'''

from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel): #pydantic model
    name: str
    email: str
    rollno : int

my_posts = [{"name":"kirti","email":"kirti@gmail.com","rollno":1}]

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
    my_posts.append(post_dict)
    return {"data":post_dict}

def find_post(rollno):
    for p in my_posts:
        if p["rollno"] == int(rollno):
            return p 

def find_index_post(rollno):
    for i, p in enumerate(my_posts):
        if p['rollno'] == int(rollno):
            return i
        

@app.get("/posts/{rollno}")
def get_post(rollno: int):
    post = find_post(rollno)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with rollno: {rollno} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id: {id} was not found"}
    return {"post-details": post}


@app.delete("/posts/{rollno}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(rollno: int):
    index = find_index_post(rollno)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with rollno {rollno} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{rollno}")
def update_record(rollno: int, post: Post):
    index = find_index_post(rollno)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with rollno {rollno} does not exist")
    post_dict = post.dict()
    post_dict['rollno'] = rollno
    my_posts[index] = post_dict

    return {"data":post_dict}
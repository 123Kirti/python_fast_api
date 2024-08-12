from fastapi import FastAPI
app = FastAPI()



#request get method url: "/"
@app.get("/") #get http method [just a path to execute the code][\ is for the root path, this refers to the path we need to go or visit]
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post."}
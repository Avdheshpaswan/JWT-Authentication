import uvicorn 
from fastapi import FastAPI,HTTPException
from app.model import PostSchema

posts=[
    {
        "id":1,
        "title":"python",
        "content":"python is easy to learn"
    },
    {
        "id":2,
        "title":"friends",
        "content":"great company of friends is hard to find"
    },
    {
        "id":3,
        "title":"netflix",
        "content":"netflix is ocean of movies and shows to watch around the globe"
    },
    {
        "id":4,
        "title":"AI-Era",
        "content":"advancement in latest tech world has boosted the development multifolds in future"
    }    
]

app=FastAPI()

# get endpoint for testing
@app.get("/",tags=["demo"])
def get_data():
    return {"welcome":"user"}

# get endpoint for retrieving all posts
@app.get("/posts",tags=["posts"])
def get_posts():
    return {"data":posts}

# get endpoint for retrieving specific id post
@app.get("/posts/{id}",tags=["posts"])
def get_specific_post(id:int):
    if id > len(posts):
        return {
            "error":"post with ID does not exist!"
        } 

    for post in posts:
        if post["id"]==id:
            return {"data":post}


#post endpoint to create newpost
@app.post("/posts",tags=["posts"])
def add_post(post:PostSchema):
    post.id=len(posts)+1;
    posts.append(post.__dict__)

    return {"msg":"New post added"}  
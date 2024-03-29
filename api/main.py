import pymongo
from pymongo import MongoClient
from fastapi import FastAPI
from fastapi import HTTPException

from model_classes import *
from typing import List

# Connecting to mongo client

client = MongoClient(
    host="localhost", port=27017, username="mongoadmin", password="turbit!"
)

db = client["jsonplaceholder"]

# Expose with FastAPI, define GET methods for all endpoints
app = FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    client.close()


# Endpoints for whole directories first
@app.get("/posts", response_model=List[Post])
async def show_posts():
    allposts = db.posts.find({})
    return allposts


@app.get("/albums", response_model=List[Album])
async def show_albums():
    allalbums = db.albums.find({})
    return allalbums


@app.get("/comments", response_model=List[Comment])
async def show_comments():
    allcomments = db.comments.find({})
    return allcomments


@app.get("/photos", response_model=List[Photo])
async def show_photos():
    allphotos = db.photos.find({})
    return allphotos


@app.get("/todos", response_model=List[Todo])
async def show_todos():
    alltodos = db.todos.find({})
    return alltodos


@app.get("/users", response_model=List[User])
async def show_users():
    allusers = db.users.find({})
    return allusers


@app.get("/counts", response_model=List[Count])
async def show_counts():
    allcounts = db.counts.find({})
    return allcounts


# Endpoints for single items
@app.get("/posts/{id}", response_model=Post)
async def read_post(id: int):
    post = db.posts.find_one({"id": id})
    if post is not None:
        return post
    raise HTTPException(status_code=404, detail=f"Post {id} not found")


@app.get("/comments/{id}", response_model=Comment)
async def read_cmnt(id: int):
    comment = db.comments.find_one({"id": id})
    if comment is not None:
        return comment
    raise HTTPException(status_code=404, detail=f"Comment {id} not found")


@app.get("/todos/{id}", response_model=Todo)
async def read_todo(id: int):
    todo = db.todos.find_one({"id": id})
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail=f"Todo {id} not found")


@app.get("/albums/{id}", response_model=Album)
async def read_album(id: int):
    album = db.albums.find_one({"id": id})
    if album is not None:
        return album
    raise HTTPException(status_code=404, detail=f"Album {id} not found")


@app.get("/photos/{id}", response_model=Photo)
async def read_pic(id: int):
    photo = db.photos.find_one({"id": id})
    if photo is not None:
        return photo
    raise HTTPException(status_code=404, detail=f"Photo {id} not found")


@app.get("/users/{id}", response_model=User)
async def read_usr(id: int):
    user = db.users.find_one({"id": id})
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")


@app.get("/counts/{userId}", response_model=Count)
async def read_count(userId: int):
    count = db.counts.find_one({"userId": userId})
    if count is not None:
        return count
    raise HTTPException(status_code=404, detail=f"User Id {userId} not found")

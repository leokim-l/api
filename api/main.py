import pymongo
import json
from pymongo import MongoClient
import requests
import bs4
from urllib.request import urlretrieve
import pprint
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
import numpy as np


# EXTRA CREDIT
# (5) Maybe in the README
# (cogli l'occasione per imparare come si può mostrare il contenuto di github in modo fancy)
# write: suppongo che abbiate bla bla (mongodb, poetry, git, docker-compose) installato, dopo aver git pullato fate poetry (?) install(?),
# poi qlcs tipo setup.sh che sovrascriva la riga VOLUMES di file yaml, poi docker up -d dalla cartella giusta (o addiritura lo posso mettere in questo file python così basta fare `$HOME/.local/bin/poetry run main.py` e fa tutto da solo? Potrei farlo con os, altrimenty c'è docker-py che è per Docker Engine API, import docker :P) controlla il container con docker ps, poi fai che runnare main.py
#
# (6) Put stuff in the test folder, look at some test driven development stuff and understand what is important to be tested. Then put this stuff in readme so ppl know that, instead of/besides running main.py, they can run test1.py, test2.py, ..., tests1-5.py or whatever I learn when reading about TDD :D <3
# ==========================================================================
# Setup
url = "https://jsonplaceholder.typicode.com"
local_db = "/home/leonardo/Desktop/programs/turbit/api/database/"
data_src = ["posts", "comments", "albums", "photos", "todos", "users"]
data_src = ["/" + src for src in data_src]
req = requests.get(url)
data = bs4.BeautifulSoup(req.text, "html.parser")
links = [
    url + lst.get("href") for lst in data.find_all("a") if lst.get("href") in data_src
]
links = list(np.unique(np.array(links)))  # list(set(links))  # unique
fn = [name.split("/")[-1] for name in links]

# ==========================================================================
# Connect to mongodb instance running in docker
client = MongoClient(
    host="localhost", port=27017, username="mongoadmin", password="turbit!"
)

db = client["jsonplaceholder"]

# ==========================================================================
# Download data and put it in MongoDB
for i in range(len(links)):
    fname = local_db + fn[i] + ".json"
    urlretrieve(links[i], fname)
    with open(fname, "r") as myfile:
        file_tmp = json.load(myfile)
        if isinstance(file_tmp, list):
            db[fn[i]].insert_many(file_tmp)
        else:
            db[fn[i]].insert_one(file_tmp)
    del file_tmp

# Here goes the code that counts posts and comments of each userId
# cursor = db.posts.find({"userId": 1}).limit(10)
# for doc in cursor:
#    pprint.pprint(doc)

# create new endpoint named "/counts" with userId, numPosts, numComments. Maybe not necessary


# Expose with FastAPI
app = FastAPI()


# Make insgesamt 7 classes
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class Album(BaseModel):
    userId: int
    id: int
    title: str


class Photo(BaseModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: {street: str, suite: str}
    title: str
    body: str


class Count(BaseModel):
    userId: int
    numComments: int
    numPosts: int


"""
# Fix endpoint for whole folder
@app.get("/posts/", response_model=Post)
async def show_posts():
    post = db.posts.find({})
    return post
"""


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


# TODO fix User, albums, comments
@app.get("/users/{id}", response_model=User)
async def read_usr(id: int):
    user = db.users.find_one({"id": id})
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User {id} not found")


"""
@app.get("/counts/{id}", response_model=Count)
async def read_item(id: int):
    post = db.posts.find_one({"id": id})
    if post is not None:
        return post
    raise HTTPException(status_code=404, detail=f"Post {id} not found")
"""

# client.close()

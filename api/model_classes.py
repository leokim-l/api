from pydantic import BaseModel


# Make altogether 7 models, + submodules for users
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


# users' submodels
class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str


class Count(BaseModel):
    userId: int
    numComments: int
    numPosts: int

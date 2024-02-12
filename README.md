## Small project/exercise about developing APIs with Docker, Python and MongoDB

# Task descritpion (refer to DESCRIPTION.md for more details):
# Develop a pipeline that involves setting up a MongoDB database using Docker Compose, retrieving and storing data from an external API, and exposing this data through FastAPI.

1. Setup MongoDB with Docker Compose
Use Docker Compose to set up a MongoDB database.

2. Data Retrieval and Loading into MongoDB
Retrieve data from the JSONPlaceholder - Free Fake REST API and store it in MongoDB with python.

3. Create a RESTful API with FastAPI
Develop a FastAPI application to provide access to the mongo data. Include an endpoint to report the total number of posts and comments for each user.

## Usage

It is assumed that poetry and docker-compose are installed on the system. Once that is complete, after cloning the repository, change the relevant paths in docker-compose.yml and simply run, from the project folder:

-- docker-compose up -d

Then, import the data through:

-- python3 api/import_data_to_db.py

Run the API by executing, from within the api/ folder:

-- poetry run uvicorn main:app --reload

Now the database is up and running. Open your browser at

http://127.0.0.1:8000/

and try to see what happens if looking for the folder: posts, comments, albums, photos, todos, users, counts.
Also, at those endpoints, one can query by id, for instance:

http://127.0.0.1:8000/posts/23

will show the "post" with id 23, if it exists. 


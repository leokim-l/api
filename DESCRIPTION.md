# A short description of the project

The structure is very simple, with a docker-compose file (`docker-compose.yml`) in the main folder to run a MongoDB instance in docker. The directory /api contains three relevant scripts:

1. api/import_data_to_db.py, to be run once, which connects to the MongoDB client, downloads the data from the web and populates the database, with one endpoint per category (posts, comments,...). Here, the "counts" endpoint is created as a separate collection for simplicity, although the better approach of moving this to functions within FastAPI is used in task 2.

2. api/model_classes.py contains the pydantic response models, plus submodules for users.

3. api/main.py finally creates a FastAPI instance, with a trivial shutdown application and 14 other apps for GET methods as endpoints. Two per category of JSONPlaceholder - Free FakeREST API , i.e. users, comments, etc. , plus two for the `counts` endpoint. One can query by path (e.g. `/users') and get the full list, or by the relevant id (e.g. `/users/12`).

# Still todo/improvements:

1. Get rid of explicit paths in docker-compose.yml, which should be trivial, but would not always work if simply substituting by ${PWD}.

2. The point mentioned above in 1., namely not generating extra data for the `/counts` endpoint.

3. There is a small error in the task, namely there is no connection between comments and users, it is simply not a feature of the dataset. Thus counting comments per user, done here via email, always gives 0. One could count comments per post.

4. Add tests.

import json
from pymongo import MongoClient
import requests
import bs4
from urllib.request import urlretrieve
import numpy as np

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
# num_posts = db.posts.count_documents({"userId": userId})
unique_usrs = db.users.distinct("id")
counts_data = []
for usr in unique_usrs:
    num_posts = db.posts.count_documents({"userId": usr})
    usr_email = db.usrs.find_one({"email": usr})
    num_comments = db.comments.count_documents({"email": usr_email})
    counts_data.append(
        {"userId": usr, "numComments": num_comments, "numPosts": num_posts}
    )
if isinstance(counts_data, list):
    db["counts"].insert_many(counts_data)
else:
    db["counts"].insert_one(counts_data)


client.close()

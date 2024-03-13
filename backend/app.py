from flask import Flask,redirect,render_template,url_for
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient

import datetime

import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
CORS(app)

MONGO_URI = "mongodb://localhost:27017/mydatabase"

# Defining the MongoDB client
client = MongoClient(MONGO_URI)

# Set up the database and collection
db = client['db']  # database name, 'db'
store = db['store']  # collection name, 'store'

@app.route("/save/<path:link>",methods=['GET','POST', 'OPTIONS'])
def save(link):
    print(link)
    dt=datetime.datetime.now()

    uid=unique()
    while(store.find_one({"_id":uid}) is not None):
        uid=unique()

    link=link_prep(link)

    print(link)
    print(uid)
    print(dt)
    store.insert_one({"long_url":link,"_id":uid,"date":dt})#short_url is the _id 'PK'
    return {'short_url':uid}


@app.route("/go/<path:code>",methods=["GET"])
def go(code):
    real_url=store.find_one({"_id":code})
    print(real_url)
    a=real_url['long_url']
    print(a)
    return redirect(a)

@app.route("/")
def hello_world():
    store.insert_one({"a":1})
    return "Hello World"


def link_prep(code):

    if "youtube.com/watch?v=" in code:
        # Extract the video ID from the URL
        video_id = code.split("watch?v=")[1]
        # Construct the URL for the embedded video
        youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
        print("YouTube direct:", youtube_embed_url)
        return youtube_embed_url
        return redirect(youtube_embed_url)

    elif code.startswith("https://") or code.startswith("http://"):
        # If it does, directly redirect to the full URL

        print("Direct Redirect:", code)
        return code
        return redirect(code)
    
    # If it doesn't have https://
    full_url = "https://" + code
    print("Modified URL:", full_url)
    return full_url
    return redirect(full_url)



def unique():
    id=str(uuid.uuid4())[:4]
    return id

app.run(debug=True)

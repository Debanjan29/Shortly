from flask import Flask,redirect,render_template,url_for

from flask_pymongo import PyMongo
from flask_pymongo import MongoClient

import datetime

import uuid

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

MONGO_URI = "mongodb://localhost:27017/mydatabase"

# Defining the MongoDB client
client = MongoClient(MONGO_URI)

# Set up the database and collection
db = client['db']  # database name, 'db'
store = db['store']  # collection name, 'store'

@app.route("/get/<path:link>",methods=['GET'])
def get(link):
    print(link)
    dt=datetime.datetime.now()
    store.insert_one({"long_url":link,"_id":187,"date":dt})#short_url is the _id 'PK'
    return redirect(link)


@app.route("/")
def hello_world():
    store.insert_one({"a":1})
    return "Hello World"

@app.route("/<stringi>")
def goto(stringi):
    if stringi=='abc':
        a="https://www.w3schools.com"
        return redirect(a)
    return "redirect(url_for())"

@app.route("/go/<path:code>")
def go(code):

    #if "watch?v=" in code and code.startswith("https://"):
        #id=code.split("watch?v=")[1]
        #final_url="https://youtube.com/embed/"+id
        #print("Youtube direct",final_url)
        #return redirect(final_url)

    if "youtube.com/watch?v=" in code:
        # Extract the video ID from the URL
        video_id = code.split("watch?v=")[1]
        # Construct the URL for the embedded video
        youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
        print("YouTube direct:", youtube_embed_url)
        return redirect(youtube_embed_url)

    elif code.startswith("https://") or code.startswith("http://"):
        # If it does, directly redirect to the full URL

        print("Direct Redirect:", code)
        return redirect(code)
    
    # If it doesn't have https://
    full_url = "https://" + code
    print("Modified URL:", full_url)
    return redirect(full_url)
    return redirect("https://"+a+".com")
    if code=="gfr":
        return redirect()
    return "hi"+"  "+code


def unique():
    id=uuid.uuid4[4]
    return id

app.run(debug=True)

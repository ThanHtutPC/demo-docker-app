from flask import Flask
from pymongo import MongoClient
from retrying import retry

app = Flask(__name__)

@retry(stop_max_attempt_number=10, wait_fixed=2000)
def connect_to_mongo():
    client = MongoClient('mongodb://mongo:27017/')
    return client.test_database

db = connect_to_mongo()

@app.route('/')
def hello_world():
    # Insert a document into MongoDB
    db.test_collection.insert_one({"message": "Hello, World!"})
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


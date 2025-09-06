from flask import Flask, jsonify, request
from pymongo import MongoClient
import os


app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/testdb")
client = MongoClient(MONGO_URI)
db = client.get_database()


@app.route("/")
def home():
    return jsonify({"message": "Flask + MongoDB is working!"})

@app.route("/add", methods=["POST"])
def add_document():
    data = request.json
    result = db.items.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)})

@app.route("/items", methods=["GET"])
def get_items():
    items = list(db.items.find({}, {"_id": 0}))
    return jsonify(items)


if __name__ == "__main__":
    # enable debug=True for auto-reload
    app.run(host="0.0.0.0", port=5000, debug=True)
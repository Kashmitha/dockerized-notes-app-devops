from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# connect to redis container
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def home():
    return "Notes API running"

@app.route("/add", methods=["POST"])
def add_note():
    note = request.json["note"]
    redis_client.rpush("notes", note)
    return jsonify({"message": "Note added"})

@app.route("/notes", methods=["GET"])
def get_notes():
    notes = redis_client.lrange("notes", 0, -1)
    return jsonify(notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
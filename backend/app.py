from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

@app.route("/search")
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "key": YOUTUBE_API_KEY,
        "maxResults": 5
    }

    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    data = response.json()

    # Filter out YouTube Shorts by checking if 'shorts' is in the video title or description
    filtered_items = [
        item for item in data.get("items", [])
        if "shorts" not in item["snippet"]["title"].lower()
        and "shorts" not in item["snippet"]["description"].lower()
    ]

    return jsonify({"items": filtered_items})
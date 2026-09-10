"""
Minimal Flask starter API.

Run locally:
    pip install -r requirements.txt
    python app/main.py

Then open http://localhost:5000/ or http://localhost:5000/api/hello?name=Dan
"""

from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def index():
    """Simple landing route so the app isn't just an empty shell."""
    return jsonify(
        {
            "project": "hackathon-starter",
            "status": "ok",
            "message": "API is running. Try GET /api/hello?name=YourName",
        }
    )


@app.get("/health")
def health():
    """Basic health check endpoint, handy for judges/CI to verify the app boots."""
    return jsonify({"status": "healthy", "time": datetime.now(timezone.utc).isoformat()})


@app.get("/api/hello")
def hello():
    """Example endpoint: greets whoever is calling it."""
    name = request.args.get("name", "world")
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)

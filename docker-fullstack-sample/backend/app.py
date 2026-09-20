from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Docker Backend is running!"})

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello from Python Flask Backend!",
        "status": "success"
    })

@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

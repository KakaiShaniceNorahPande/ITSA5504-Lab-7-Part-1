from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello Cloud", 200

@app.route("/hello")
def hello():
    return jsonify(message="Hello Cloud"), 200

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/greet")
def greet():
    return "<h1>Welcome Shanice</h1>", 200

@app.route("/")
def root():
    return "Welcome to ITSA5504 Exercise 7", 200

@app.route("/hello")
def hello():
    return jsonify(message="Hello Cloud | ITSA5504 | Exercise 7"), 200

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

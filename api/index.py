from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Vercel entry point
def handler(environ, start_response):
    return app(environ, start_response)

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask is working on Vercel!"

# Vercel entry point
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

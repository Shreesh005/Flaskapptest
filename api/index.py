from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask is working on Vercel!"

# 🔧 Export WSGI-compatible handler for Vercel
handler = app.wsgi_app

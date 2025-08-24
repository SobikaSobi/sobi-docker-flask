from flask import Flask, jsonify, render_template
import datetime as dt
import os

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify(status="ok", service="flask-docker-starter", time=dt.datetime.utcnow().isoformat() + "Z")

@app.get("/api/ping")
def ping():
    return jsonify(ping="pong", at=dt.datetime.utcnow().isoformat() + "Z")

if __name__ == "__main__":
    # Set host to 0.0.0.0 so Docker can expose it
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

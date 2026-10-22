from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "uptime monitor is running"
@app.get("/health")
def health():
    return {"status":"ok"}

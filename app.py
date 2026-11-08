import os

import psycopg
from flask import Flask

app = Flask(__name__)


def get_conn():
    return psycopg.connect(os.environ["DATABASE_URL"])


@app.get("/")
def home():
    return "Uptime monitor is running"


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/visits")
def visits():
    with get_conn() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS visits "
            "(id serial PRIMARY KEY, at timestamptz DEFAULT now())"
        )
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        n = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return {"visits": n}

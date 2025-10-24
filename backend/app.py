from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = "profile.db"

def query_db(query, args=(), one=False):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

# Serve frontend
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/profile")
def get_profile():
    profile = query_db("SELECT * FROM profile LIMIT 1", one=True)
    skills = [r["name"] for r in query_db("SELECT name FROM skills")]
    return jsonify({**dict(profile), "skills": skills})

@app.route("/projects")
def get_projects():
    skill = request.args.get("skill")
    if skill:
        rows = query_db("SELECT * FROM projects WHERE skill LIKE ?", (f"%{skill}%",))
    else:
        rows = query_db("SELECT * FROM projects")
    return jsonify([dict(r) for r in rows])

@app.route("/search")
def search():
    q = f"%{request.args.get('q','')}%"
    rows = query_db("SELECT * FROM projects WHERE title LIKE ? OR description LIKE ?", (q, q))
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True)

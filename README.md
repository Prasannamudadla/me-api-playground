# Me-API Playground

Minimal portfolio API + frontend (Flask + SQLite + plain HTML/JS).  
Shows profile, skills, projects and supports queries (filter by skill, search). Deployed on Render.

---

## Live & Repo
- **Live app:** https://me-api-playground-n4p7.onrender.com
- **GitHub:** https://github.com/Prasannamudadla/me-api-playground
- **Resume:** [View Resume](https://drive.google.com/file/d/19nXg7YxzvSeZdBdbchzi0cn9CvDwwdkh/view?usp=sharing)


---

## Quick Summary / Acceptance
- GET `/health` → liveness (200).  
- GET `/profile` → returns profile + skills.  
- GET `/projects` → list projects; `?skill=<name>` filters.  
- GET `/search?q=<term>` → search projects by title/description.  
- Frontend (served at `/`) calls the hosted API; CORS enabled.

---

## Tech Stack
- Backend: **Flask**, Python  
- DB: **SQLite** (seeded via `seed.py`)  
- Frontend: plain **HTML / CSS / JS** (served by Flask `templates` / `static`)  
- Hosting: **Render** (single web service)

---

## Project layout

backend/               
│
├── app.py              # main Flask backend (runs the API + serves frontend)
├── schema.sql          # defines your database tables
├── seed.py             # creates & seeds the database
├── requirements.txt    # contains Flask, gunicorn, flask-cors, etc.
│
├── templates/          # HTML frontend
│   └── index.html
│
├── static/             # CSS & JS
│   ├── style.css
│   └── script.js
│
└── README.md  
## 🗃️ Database Schema

**schema.sql**
```sql
CREATE TABLE profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    education TEXT,
    github TEXT,
    linkedin TEXT,
    leetcode TEXT
);

CREATE TABLE skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    skill TEXT,
    github_link TEXT
);
```

---

## Setup (local)

```bash
git clone https://github.com/Prasannamudadla/me-api-playground.git
cd me-api-playground
cd backend 

# (recommended: create and activate virtualenv)
pip install -r requirements.txt

# create & seed DB (profile, skills, projects)
python seed.py

# run app
python app.py
# open http://127.0.0.1:5000
```

## Architecture

- Flask app exposes RESTful APIs.

- SQLite used as local lightweight DB.

- Static frontend served via Flask templates.

- CORS enabled for API consumption.

- Gunicorn used in production on Render.

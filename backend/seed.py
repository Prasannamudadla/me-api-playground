import sqlite3

con = sqlite3.connect("profile.db")
cur = con.cursor()
cur.executescript(open("schema.sql").read())

# Profile
cur.execute("""
INSERT INTO profile (name, email, education, github, linkedin, leetcode)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    "Mudadla Sai Prasanna",
    "saiprasanna.mudadla26@gmail.com",
    "B.Tech, Computer Science and Engineering, IIT Goa (2022–2026)",
    "https://github.com/Prasannamudadla",
    "https://linkedin.com/in/mudadla-sai-prasanna",
    "https://leetcode.com/u/Prasanna48/"
))

# Skills
skills = [
    "Python", "C", "C++", "HTML", "CSS", "JavaScript", "React",
    "SQL", "SQLite", "Flask", "Tailwind CSS", "Latex"
    "Git", "Linux", "Data Structures and Algorithms"
]
cur.executemany("INSERT INTO skills (name) VALUES (?)", [(s,) for s in skills])

# Projects
projects = [
    (
        "Implementation of Congestion Control Algorithms",
        "Python simulation comparing congestion control algorithms and analyzing key metrics like retransmissions and ACKs.",
        "Python, Networking",
        "https://github.com/Prasannamudadla/Congestion-Control-Algorithms"
    ),
    (
        "CodeBook – DSA Progress Tracker",
        "Flask web app to track DSA problems with authentication and CRUD operations using SQLite.",
        "Python, Flask, SQLite, HTML, CSS, Jinja2",
        "https://github.com/Prasannamudadla/codebook-flask-app"
    ),
    (
        "Coffee Shop Web App",
        "React + Tailwind app with reusable components, product listing, cart, and checkout functionality.",
        "React, Tailwind CSS, JavaScript",
        "https://github.com/Prasannamudadla/coffee-shop-web-app"
    ),
    (
        "M.Tech Admission Automation (BTP)",
        "PySide6 desktop application for automating M.Tech admission seat allocation and Excel report generation.",
        "Python, SQLite, PySide6",
        "https://github.com/Prasannamudadla/BTP-MTech-Admissions"
    ),
    (
        "SMS Spam Classifier",
        "Streamlit ML app classifying SMS as spam or ham with Naive Bayes achieving 97% accuracy.",
        "Python, scikit-learn, Streamlit",
        "https://github.com/Prasannamudadla/SMS-Spam-Classifier"
    ),
]
cur.executemany("INSERT INTO projects (title, description, skill, github_link) VALUES (?, ?, ?, ?)", projects)

con.commit()
con.close()
print("✅ Database seeded successfully with resume data!")

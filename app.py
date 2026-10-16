from flask import Flask, request, redirect, url_for, render_template_string
import sqlite3

app = Flask(__name__)
DATABASE = "tasks.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
        """)

PAGE = """
<h1>AWS Task Tracker</h1>
<form method="post" action="/add">
    <input name="title" placeholder="Enter a task" maxlength="200" required>
    <button type="submit">Add task</button>
</form>
<ul>
{% for task in tasks %}
    <li>{{ task }}</li>
{% else %}
    <li>No tasks yet.</li>
{% endfor %}
</ul>
"""

@app.get("/")
def home():
    with sqlite3.connect(DATABASE) as conn:
        rows = conn.execute(
            "SELECT title FROM tasks ORDER BY id DESC"
        ).fetchall()

    tasks = [row[0] for row in rows]
    return render_template_string(PAGE, tasks=tasks)

@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()

    if title and len(title) <= 200:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute(
                "INSERT INTO tasks (title) VALUES (?)",
                (title,)
            )

    return redirect(url_for("home"))
if __name__ == "__main__":
    init_db()
    app.run(debug=True)

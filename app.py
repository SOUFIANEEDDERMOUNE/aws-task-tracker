from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
tasks = []

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
    return render_template_string(PAGE, tasks=tasks)

@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    if title and len(title) <= 200:
        tasks.append(title)
    return redirect(url_for("home"))

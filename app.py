from flask import Flask, request, redirect, url_for
import sqlite3
from pathlib import Path 

app = Flask(__name__)
DB_PATH = Path("school.db")
SCHEMA_PATH = Path("schema.sql")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/init-db")
def init_db():
    """One-time setup: creates tables in school.db"""
    conn = get_db()
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    return "Database initialized ✅ (You can close this tab)"


@app.route("/")
def home():
    return redirect(url_for("students"))


@app.route("/students", methods=["GET", "POST"])
def students():
    conn = get_db()

    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()
        grade = request.form.get("grade", "").strip()
        parent_name = request.form.get("parent_name", "").strip()
        parent_phone = request.form.get("parent_phone", "").strip()

        if first_name and last_name and grade:
            conn.execute(
                """
                INSERT INTO students (first_name, last_name, grade, parent_name, parent_phone)
                VALUES (?, ?, ?, ?, ?)
                """,
                (first_name, last_name, grade, parent_name, parent_phone),
            )
            conn.commit()

        conn.close()
        return redirect(url_for("students"))

    rows = conn.execute(
        "SELECT id, first_name, last_name, grade, parent_name, parent_phone FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()

    html = """
    <h1>Students</h1>

    <h2>Add student</h2>
    <form method="post">
      <input name="first_name" placeholder="First name" required>
      <input name="last_name" placeholder="Last name" required>
      <input name="grade" placeholder="Grade" required>
      <input name="parent_name" placeholder="Parent name">
      <input name="parent_phone" placeholder="Parent phone">
      <button type="submit">Add</button>
    </form>

    <h2>Student list</h2>
    <table border="1" cellpadding="6" cellspacing="0">
      <tr>
        <th>ID</th><th>Name</th><th>Grade</th><th>Parent</th><th>Phone</th>
      </tr>
    """
    for r in rows:
        html += f"""
        <tr>
          <td>{r['id']}</td>
          <td>{r['first_name']} {r['last_name']}</td>
          <td>{r['grade']}</td>
          <td>{r['parent_name'] or ''}</td>
          <td>{r['parent_phone'] or ''}</td>
        </tr>
        """
    html += "</table>"
    return html


if __name__ == "__main__":
    app.run(debug=True)

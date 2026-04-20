from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ✅ DB connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# ✅ CREATE TABLE (runs automatically)
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        reg_no TEXT UNIQUE,
        exam TEXT,
        score INTEGER
    )
    """)

    conn.commit()
    conn.close()

create_table()

# 🏠 INDEX PAGE
@app.route("/")
def index():
    return render_template("index.html")

# 📝 STUDENT REGISTRATION
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    reg_no = request.form["reg_no"]
    exam = request.form["exam"]

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, email, reg_no, exam) VALUES (?, ?, ?, ?)",
            (name, email, reg_no, exam)
        )
        conn.commit()
        msg = "Registration successful!"
    except:
        msg = "Registration failed! Reg No might already exist."

    conn.close()
    return msg

# 👨‍💼 ADMIN PAGE
@app.route("/admin")
def admin():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return render_template("admin.html", data=data)

# ➕ ADD / UPDATE RESULT
@app.route("/add_score", methods=["POST"])
def add_score():
    reg_no = request.form["reg_no"]
    exam = request.form["exam"]
    score = request.form["score"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET exam=?, score=? WHERE reg_no=?",
        (exam, score, reg_no)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")

# 📊 RESULT PAGE
@app.route("/result", methods=["GET", "POST"])
def result():
    student = None

    if request.method == "POST":
        reg_no = request.form["reg_no"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE reg_no=?", (reg_no,))
        student = cursor.fetchone()

        conn.close()

    return render_template("result.html", student=student)

# ▶️ RUN APP
if __name__ == "__main__":
    app.run(debug=True)
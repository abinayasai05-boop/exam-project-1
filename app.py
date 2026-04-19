from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# 🔌 DATABASE CONNECTION
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="1234",      # change your MySQL password
        database="exam_db"
    )

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

    cursor.execute(
        "INSERT INTO students (name, email, reg_no, exam) VALUES (%s, %s, %s, %s)",
        (name, email, reg_no, exam)
    )

    conn.commit()
    conn.close()

    return "Registration successful!" # go back to home


# 👨‍💼 ADMIN PAGE
@app.route("/admin")
def admin():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    conn.close()

    return render_template("admin.html", data=data)


# ➕ ADD RESULT (ADMIN)
@app.route("/add_score", methods=["POST"])
def add_score():
    reg_no = request.form["reg_no"]
    exam = request.form["exam"]
    score = request.form["score"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "UPDATE students SET exam=%s, score=%s WHERE reg_no=%s",
        (exam, score, reg_no)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")


# 📊 RESULT PAGE (SEARCH)
@app.route("/result", methods=["GET", "POST"])
def result():
    student = None

    if request.method == "POST":
        reg_no = request.form["reg_no"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students WHERE reg_no=%s", (reg_no,))
        student = cursor.fetchone()

        conn.close()

    return render_template("result.html", student=student)


# ▶️ RUN APP
if __name__ == "__main__":
    app.run(debug=True)
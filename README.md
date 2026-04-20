
# 📝 Online Exam Registration & Result Viewer

A full-stack web application built with **Flask** that allows students to register for exams and view their results. The application is deployed live on **Render**.

## 🌐 Live Demo

**Access the live website:** [https://exam-project-1-3.onrender.com](https://exam-project-1-3.onrender.com)

> ⚠️ **Note:** Being on Render's free tier, the site may take 30-50 seconds to wake up if inactive. Please wait a moment after clicking.

---

## ✨ Features

- ✅ Student Registration with unique Register Number
- ✅ Multiple Exam Subject Selection
- ✅ View Results using Register Number
- ✅ Admin Dashboard to manage all student records
- ✅ Add/Update Student Exam Scores
- ✅ SQLite Database for persistent data storage
- ✅ Mobile Responsive Design

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Flask (Python)** | Backend Web Framework |
| **SQLite** | Database |
| **HTML/CSS** | Frontend Design |
| **Gunicorn** | Production WSGI Server |
| **Render** | Cloud Deployment |

---

## 📁 Project Structure

```

exam-project-1/
├── app.py              # Main Flask application
├── database.db         # SQLite database
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html      # Registration page (Homepage)
│   ├── admin.html      # Admin dashboard
│   └── result.html     # Result viewing page
└── README.md           # Project documentation

```

---

## 🚀 Local Setup & Running

Follow these steps to run the project on your local machine:

### Prerequisites
- Python 3.8 or higher installed
- Git installed

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/abinayasai05-boop/exam-project-1.git

# 2. Navigate to project directory
cd exam-project-1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open your browser and go to:
# http://127.0.0.1:5000
```

---

📋 How to Use

For Students:

1. Open the website
2. Fill in your details in the Register for Exam form
3. Select your exam subject
4. Click Register Now
5. To view results, enter your Register Number and click Check Result

For Admin:

1. Click Go to Admin Dashboard on the homepage
2. View all registered students
3. Add or update exam scores for students
4. Changes are saved instantly to the database

---

📸 Screenshots

Registration Page Admin Dashboard Result Page
<img width="952" height="470" alt="image" src="https://github.com/user-attachments/assets/55930bba-df53-49e5-b758-fb3398566476" />


---

🔗 Repository Information

· GitHub: abinayasai05-boop/exam-project-1
· Live Demo: exam-project-1-3.onrender.com
· Author: Abinaya B

---

📝 Future Improvements

· Add user authentication for Admin
· Export data to Excel/PDF
· Email notifications for results
· Student login system
· PostgreSQL database for production

---

📄 License

This project is open source and available under the MIT License.

---

👩‍💻 Author

Abinaya B

· GitHub: @abinayasai05-boop

---

🙏 Acknowledgments

· Flask Documentation
· Render for free hosting
· SQLite for lightweight database

---

Built with ❤️ using Python and Flask
s

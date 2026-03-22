# 💼 Job Board Web Application (Django)

A full-stack job board web application built using **Django** that allows employers to post job listings and applicants to browse and apply for jobs online.

---

## 🚀 Features

### 👨‍💼 Employer

* Post new job listings
* View all jobs posted by them
* See applications received per job

### 🧑‍💻 Applicant

* Browse available jobs
* Apply for jobs online
* View status of submitted applications

### 🔐 Authentication

* User signup & login system
* Role-based access: **Employer vs Applicant**
* Secure logout with CSRF protection

---

## 🛠 Tech Stack

| Layer          | Technology                  |
| -------------- | --------------------------- |
| Backend        | Django 6                    |
| Frontend       | HTML, Bootstrap 5           |
| Database       | SQLite (default Django DB)  |
| Authentication | Django built-in auth system |

---

## 📂 Project Structure

```
jobboard/
│
├── jobboard/           # Main project settings
│
├── jobs/               # Main application
│   ├── models.py       # Job, Application, Profile models
│   ├── views.py        # Business logic
│   ├── urls.py         # App routes
│   └── templates/
│       ├── job_list.html
│       ├── add_job.html
│       ├── apply_job.html
│       ├── dashboard_employer.html
│       └── dashboard_applicant.html
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
│       └── login.html
│
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/jobboard.git
cd jobboard
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```
pip install django
```

### 4️⃣ Run migrations

```
python manage.py migrate
```

### 5️⃣ Start the server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🧪 Test Accounts

You can create users via:

```
/signup/
```

Or create a superuser:

```
python manage.py createsuperuser
```

---

## 📸 Screenshots (optional)

You can add screenshots here to improve your GitHub profile:

```
screenshots/
    home.png
    job_list.png
    dashboard.png
```

---

## 📌 Key Functionalities Explained

### Job Posting

Employers can create jobs with:

* Title
* Company
* Location
* Salary
* Description

### Job Application

Applicants submit:

* Name
* Email
* Resume link

All applications are stored and linked to the respective job.

---

## 🔐 Role-based Dashboard

| Role      | Dashboard Shows                     |
| --------- | ----------------------------------- |
| Employer  | Jobs posted + applications received |
| Applicant | Jobs applied to                     |

---

## 🧠 Learning Outcomes

This project demonstrates understanding of:

* Django Models & Relationships
* Authentication & Authorization
* Template Inheritance
* Form Handling
* CRUD operations
* Role-based UI rendering

---

## 📈 Future Improvements

* Resume file upload
* Job search & filters
* Email notifications
* Admin analytics dashboard
* REST API with Django REST Framework

---

## 👨‍💻 Author

**Rajshekhar Singh**

If you found this useful or used it for learning, feel free to ⭐ the repo.

---

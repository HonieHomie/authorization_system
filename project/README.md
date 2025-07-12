# Django Simple Authorization System

A lightweight starter project that adds token-based user authentication and role-based authorization to any Django 4.x app.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| Role-Based Access | Custom IsRole DRF permission class for fine-grained endpoint protection. |
| User Management API | Register, log in/out, change password, and view profile. |
| 100% typed | mypy-clean, with django-stubs for improved editor support. |

---

## 📦 Requirements

* Python 3.10+
* Django 4.2 LTS
* Django REST Framework 3.15+
* djangorestframework-simplejwt 5.x

---

## 🚀 Quickstart

```bash
# 1. Clone
git clone https://github.com/yourname/django-authz-simple.git
cd django-authz-simple

# 2. Create env
python -m venv .venv
source .venv/bin/activate

# 3. Install deps
pip install -r requirements.txt

# 4. Environment variables
cp .env.example .env  # edit as needed

# 5. Run migrations & create admin
python manage.py migrate
python manage.py createsuperuser

# 6. Launch
python manage.py runserver 0.0.0.0:8000

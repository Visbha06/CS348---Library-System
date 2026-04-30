# Library Management System

A Django-based library management system that supports:
- Managing books and genres
- Filtering and reports
- CRUD operations
- Protection against SQL injection
- Transactions and indexing

## Tech Stack
- Python 3.10
- Django 5.x
- SQLite (development)

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

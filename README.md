# Expense Manager System

A Django-based Expense Manager application that allows users to manage daily expenses through both Web UI and REST APIs.

The application follows a layered architecture using Django Forms, Services, and Django REST Framework to ensure clean code, maintainability, and scalability.

---

## Features

- Create Expense
- Update Expense
- Delete Expense
- View Expense List
- Search Expenses
- Form Validation
- REST API Support
- Custom Exception Handling
- Logging Support
- MySQL Database Integration
- Django Admin Panel

---

## Technology Stack

### Backend
- Python 3.x
- Django
- Django REST Framework

### Database
- MySQL

### Frontend
- HTML
- CSS
- Django Templates

### Other Tools
- Logging
- Git
- GitHub

---

## Project Architecture

The project follows a layered architecture:

### 1. Presentation Layer

Responsible for handling user requests.

Files:
- views.py
- forms.py
- templates/

Responsibilities:
- Render pages
- Handle form submissions
- Validate user input

---

### 2. Service Layer

Responsible for business logic.

File:
- services.py

Responsibilities:
- Expense calculations
- Business validations
- Communication between views and models

---

### 3. Data Layer

Responsible for database operations.

File:
- models.py

Responsibilities:
- Define database schema
- ORM operations

---

### 4. API Layer

Provides REST API functionality.

Files:
- serializers.py
- api_views.py
- api_urls.py
- exceptions.py

Responsibilities:
- JSON serialization
- API endpoints
- API validations
- Error handling

---

## Database Model

### Expense

| Field | Type |
|---------|---------|
| id | Auto Increment Primary Key |
| title | CharField |
| category | CharField |
| amount | DecimalField |
| description | TextField |
| expense_date | DateField |
| created_at | DateTimeField |

---

## Folder Structure

expense_manager_system/
│
├── api/
│   ├── api_urls.py
│   ├── api_views.py
│   ├── serializers.py
│   └── exceptions.py
│
├── expensesApp/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── logging_config.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── expense_tracker/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/
│
├── manage.py
│
└── expense.log

---

## Installation

### Clone Repository

git clone <repository-url>

cd expense_manager_system

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## Database Configuration

Configure MySQL in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'expense_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

---

## Run Migrations

python manage.py makemigrations

python manage.py migrate

---

## Create Admin User

python manage.py createsuperuser

---

## Run Server

python manage.py runserver

Application:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

---

## API Endpoints

GET /api/expenses/

GET /api/expenses/<id>/

POST /api/expenses/

PUT /api/expenses/<id>/

DELETE /api/expenses/<id>/

---

## Logging

The application uses custom logging configuration.

Log File:

expense.log

Features:

- Request Logging
- Error Logging
- Exception Tracking

---

## Future Enhancements

- User Authentication
- JWT Authentication
- Expense Analytics Dashboard
- Monthly Reports
- Export to Excel
- Export to PDF
- Budget Management
- Category Management

---

## Learning Outcomes

- Django MVT Architecture
- Django Forms
- Service Layer Pattern
- Django ORM
- MySQL Integration
- REST APIs
- Serialization
- Exception Handling
- Logging
- Clean Architecture Principles

---

## Author

Amol
Python Developer

# Django Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Total Apps](#total-apps)
3. [Project Structure](#project-structure)
4. [How Project is Created](#how-project-is-created)
5. [How Apps are Created](#how-apps-are-created)
6. [Request Flow (GET/POST)](#request-flow-getpost)
7. [Database Schema](#database-schema)
8. [App Details](#app-details)
9. [URL Routing System](#url-routing-system)
10. [Key Concepts](#key-concepts)

---

## Project Overview

This is a Django web application demonstrating basic CRUD operations, authentication, and API endpoints. The project uses Django 4.2.27 and SQLite database.

---

## Total Apps

The project contains **3 custom apps**:

1. **apis** - Simple API endpoints and template rendering
2. **employee** - Employee management with database operations
3. **authentication** - User registration, login, logout, and protected pages

---

## Project Structure

```
myproject/
├── manage.py                 # Django management script
├── db.sqlite3                # SQLite database file
├── myproject/                # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── apis/                     # APIs app
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── models.py             # Database models (empty)
│   └── templates/            # HTML templates
│       ├── home.html
│       ├── addition.html
│       └── addition_result.html
├── employee/                 # Employee app
│   ├── views.py              # View functions
│   ├── urls.py               # URL routing
│   ├── models.py             # Employee model
│   └── templates/
│       └── employeeForm.html
└── authentication/           # Authentication app
    ├── views.py              # View functions
    ├── urls.py               # URL routing
    ├── models.py             # Models (empty, uses Django's User)
    └── templates/
        ├── register.html
        ├── login.html
        └── home.html
```

---

## How Project is Created

### Step 1: Create Django Project
```bash
django-admin startproject myproject
```
This creates:
- `myproject/` directory (project configuration)
- `manage.py` (Django management script)
- `settings.py` (project settings)
- `urls.py` (main URL routing)

### Step 2: Create Database
```bash
python manage.py migrate
```
Creates initial database tables for Django's built-in apps (admin, auth, sessions, etc.)

### Step 3: Run Development Server
```bash
python manage.py runserver
```
Starts server at `http://127.0.0.1:8000/`

---

## How Apps are Created

### Step 1: Create App
```bash
python manage.py startapp apis
python manage.py startapp employee
python manage.py startapp authentication
```

This creates app directory with:
- `views.py` - View functions (handles requests)
- `models.py` - Database models
- `urls.py` - URL routing (created manually)
- `admin.py` - Admin configuration
- `apps.py` - App configuration
- `tests.py` - Unit tests

### Step 2: Register App in settings.py
Add app name to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'apis',
    'employee',
    'authentication',
]
```

### Step 3: Create URL Configuration
Create `urls.py` in each app and include in main `urls.py`

### Step 4: Create Templates Directory
Create `templates/` folder in each app for HTML templates

---

## Request Flow (GET/POST)

### How a Request Moves Through Django:

```
1. User Browser
   ↓ (HTTP Request: GET /api/home/)
   
2. Django Server (manage.py runserver)
   ↓
   
3. Middleware (settings.py MIDDLEWARE)
   - SecurityMiddleware
   - SessionMiddleware
   - CsrfViewMiddleware (validates CSRF token for POST)
   - AuthenticationMiddleware
   ↓
   
4. URL Routing (myproject/urls.py)
   - Matches URL pattern: "api/" → includes apis.urls
   ↓
   
5. App URL Routing (apis/urls.py)
   - Matches remaining: "home/" → calls home_page view
   ↓
   
6. View Function (apis/views.py)
   - Executes home_page(request)
   - Prepares context data
   - Renders template
   ↓
   
7. Template Engine
   - Processes home.html
   - Replaces {{ variables }} with actual values
   ↓
   
8. HTTP Response
   - Returns HTML to browser
   ↓
   
9. User Browser
   - Displays rendered page
```

### GET Request Example:
```
User visits: http://127.0.0.1:8000/api/home/

1. Browser sends GET request
2. Django routes to apis/urls.py → home_page view
3. View checks: request.method == "GET"
4. View renders template with context
5. HTML response sent to browser
```

### POST Request Example:
```
User submits form at: http://127.0.0.1:8000/db/addEmployee/

1. Browser sends POST request with form data
2. CSRF middleware validates token
3. Django routes to employee/urls.py → addEmployee view
4. View checks: request.method == "POST"
5. View extracts data from request.POST
6. View creates Employee object
7. View saves to database
8. HTTP response sent to browser
```

---

## Database Schema

### Employee Table
Created by `employee/models.py`:
```sql
CREATE TABLE employee_employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    birthDate DATE NOT NULL
);
```

### Django Built-in Tables
- `auth_user` - User accounts (used by authentication app)
- `django_session` - User sessions
- `django_migrations` - Migration history
- `django_admin_log` - Admin action logs

### Creating Database Tables
```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

---

## App Details

### 1. APIs App (`apis/`)

**Purpose**: Demonstrates simple views, template rendering, and form handling

**URLs** (prefixed with `/api/`):
- `/api/hello/` - Simple text response
- `/api/home/` - Template with dynamic data
- `/api/add/` - Calculator (GET: form, POST: result)

**Views**:
- `greet_view()` - Returns plain text
- `home_page()` - Renders template with context variables
- `add_numbers()` - Handles GET (form) and POST (calculation)

**Templates**:
- `home.html` - Displays name, age, skills list
- `addition.html` - Calculator input form
- `addition_result.html` - Shows calculation result

**Use Cases**:
- Learning template rendering
- Understanding context variables
- Form submission handling

---

### 2. Employee App (`employee/`)

**Purpose**: Demonstrates database operations (CRUD) with models

**URLs** (prefixed with `/db/`):
- `/db/getEmployees/` - GET: Returns all employees as JSON
- `/db/addEmployee/` - GET: Shows form, POST: Saves employee

**Views**:
- `getEmployeeList()` - Queries database, returns JSON
- `addEmployee()` - GET: shows form, POST: saves to database

**Model**:
- `Employee` - name, age, birthDate fields

**Database Operations**:
- `Employee.objects.all()` - Get all records
- `Employee.objects.create()` - Create new record
- `employee.save()` - Save to database

**Use Cases**:
- Database CRUD operations
- JSON API endpoints
- Form-to-database workflow

---

### 3. Authentication App (`authentication/`)

**Purpose**: User registration, login, logout, and protected pages

**URLs** (prefixed with `/auth/`):
- `/auth/register/` - GET: form, POST: create user
- `/auth/login/` - GET: form, POST: authenticate
- `/auth/logout/` - Logout user
- `/auth/home/` - Protected page (requires login)

**Views**:
- `register_view()` - Creates new user account
- `login_view()` - Authenticates and creates session
- `logout_view()` - Destroys session
- `home_view()` - Protected page with `@login_required`

**Authentication Flow**:
1. User registers → account created in `auth_user` table
2. User logs in → `authenticate()` verifies credentials
3. `login()` creates session → user stays logged in
4. Protected pages check `@login_required` decorator
5. User logs out → `logout()` destroys session

**Use Cases**:
- User authentication
- Session management
- Protected routes
- Login/logout functionality

---

## URL Routing System

### Main URLs (`myproject/urls.py`)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("apis.urls")),      # /api/* → apis app
    path("db/", include("employee.urls")),   # /db/* → employee app
    path("auth/", include("authentication.urls")),  # /auth/* → authentication app
]
```

### How URL Matching Works:
1. User visits: `http://127.0.0.1:8000/api/home/`
2. Django checks `myproject/urls.py`
3. Matches `"api/"` prefix → includes `apis.urls`
4. Django checks `apis/urls.py`
5. Matches `"home/"` → calls `home_page` view

### URL Names:
- `name="home"` allows referencing: `{% url 'home' %}` or `redirect('home')`
- Makes URLs maintainable (change URL without breaking code)

---

## Key Concepts

### 1. Models (Database)
- Define database structure
- Django ORM converts to SQL
- Located in `app/models.py`

### 2. Views (Request Handlers)
- Handle HTTP requests
- Process data
- Return responses
- Located in `app/views.py`

### 3. URLs (Routing)
- Map URLs to views
- Located in `app/urls.py`
- Included in main `urls.py`

### 4. Templates (HTML)
- Dynamic HTML pages
- Use Django template language
- Located in `app/templates/`

### 5. CSRF Protection
- Prevents Cross-Site Request Forgery
- Required for POST requests
- Add `{% csrf_token %}` in forms
- Use `@csrf_protect` decorator

### 6. Sessions
- Store user data across requests
- Created by `login()` function
- Destroyed by `logout()` function
- Available via `request.user`

### 7. Decorators
- `@csrf_protect` - Validates CSRF token
- `@login_required` - Requires user to be logged in

---

## Running the Project

### Initial Setup:
```bash
# Install Django (if not installed)
pip install django

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (for admin)
python manage.py createsuperuser

# Run server
python manage.py runserver
```

### Access URLs:
- Admin: http://127.0.0.1:8000/admin/
- APIs: http://127.0.0.1:8000/api/home/
- Employees: http://127.0.0.1:8000/db/addEmployee/
- Auth: http://127.0.0.1:8000/auth/login/

---

## Summary

This project demonstrates:
- ✅ Django project and app creation
- ✅ URL routing and request handling
- ✅ Template rendering with context
- ✅ Database models and CRUD operations
- ✅ Form handling (GET/POST)
- ✅ User authentication and sessions
- ✅ Protected routes with decorators
- ✅ JSON API endpoints

Perfect for beginners to understand Django's core concepts and request-response cycle!

# Django-project-restAPI-with-auth

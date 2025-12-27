# URL routing for authentication app - accessed via /auth/register/, /auth/login/, etc.
from django.urls import path, include
from employee.views import getEmployeeList
from employee.views import addEmployee
from authentication.views import register_view, login_view, logout_view, home_view
 # /auth/ - all URLs prefixed with /auth/ from main urls.py
urlpatterns = [
    path("register/", register_view, name="register"),  # GET: form, POST: create user
    path("login/", login_view, name="login"),  # GET: form, POST: authenticate
    path("logout/", logout_view, name="logout"),  # Logout and redirect to login
    path("home/", home_view, name="home"),  # Protected page (requires login)
]

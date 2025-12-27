from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# User registration - GET shows form, POST creates new user account
def register_view(request):
    if request.method=="GET":
        return render(request, "register.html")  # Show registration form
    # Extract form data and create user
    username=request.POST.get("username")  # Get username from form
    password=request.POST.get("password")  # Get password from form
    # Create user in database (password automatically hashed by Django)
    User.objects.create_user(username=username, password=password)
    print("User registered with username:", username)
    return redirect("login")  # Redirect to login page after registration


# User login - GET shows form, POST authenticates and creates session
def login_view(request):
    if request.method=="GET":
        return render(request, "login.html")  # Show login form
    # Get credentials from form
    username=request.POST.get("username")  # Get username from form
    password=request.POST.get("password")  # Get password from form
    # Verify credentials against database
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # Create user session (user stays logged in)
        return redirect("home")  # Redirect to home page
    else:
        return HttpResponse("Invalid credentials")  # Show error if login fails

# User logout - destroys session and redirects to login
def logout_view(request):
    logout(request)  # Destroy user session
    return redirect("login")  # Redirect to login page

# Protected home page - only accessible to logged-in users
# @login_required automatically redirects to login if user not authenticated
@login_required
def home_view(request):
    return render(request, "home.html")  # Render home template (user is logged in)
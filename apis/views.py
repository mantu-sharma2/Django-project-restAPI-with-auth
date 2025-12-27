from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.

# Simple view that returns plain text response
def greet_view(request):
    return HttpResponse("Helo from Server")  # Returns simple text, no template needed

# Renders home.html template with dynamic data (context variables)
def home_page(request):
    # return render(request, "home.html")
    # Context dictionary - variables available in template as {{ name }}, {{ age }}, etc.
    context={
        "name": "mantu",  # String variable
        "age": 21,  # Integer variable
        "skills": ["python", "C++", "Java"],  # List - can loop with {% for %} in template
        "is_active": False  # Boolean - can use in {% if %} statements
    }
    return render(request, "home.html",context)  # Render template with context data

# Calculator view - GET shows form, POST calculates sum and shows result
@csrf_protect
def add_numbers(request):
    if request.method=="GET":
        return render(request, "addition.html")  # Show calculator form

    # Extract numbers from POST request and calculate sum
    num1=int(request.POST["num1"])  # Get first number from form
    num2=int(request.POST["num2"])  # Get second number from form
    result=num1+num2  # Calculate sum
    # Render result template with calculated result
    return render(request, "addition_result.html",context={
        "result":result  # Pass result to template as {{ result }}
    })

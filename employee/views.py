from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from employee.models import Employee

# Returns all employees as JSON - queries database and converts to JSON response
def getEmployeeList(request):
    data=Employee.objects.all().values()  # Get all employees from database as dict
    return JsonResponse({"data": list(data)})  # Return JSON response with employee data

# Handles GET (shows form) and POST (saves employee to database)
# @csrf_protect ensures form has valid CSRF token for security
@csrf_protect
def addEmployee(request):
    if request.method=="GET":
        return render(request, "employeeForm.html")  # Show form template
    if request.method == "POST":
        # Extract form data from POST request
        name=str(request.POST["name"])  # Get name from form input
        age=int(request.POST["age"])  # Get age and convert to integer
        birthDate=request.POST["birthDate"]  # Get birth date from form
        # Create Employee object in memory (not saved yet)
        employee=Employee(name=name, age=age, birthDate=birthDate)

        employee.save()  # Save to database (executes SQL INSERT)
        return HttpResponse("Employee added")
    return HttpResponse("something wrong")

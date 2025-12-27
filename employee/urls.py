# URL routing for employee app - maps URLs to view functions
from django.urls import path, include
from employee.views import getEmployeeList
from employee.views import addEmployee

# URL patterns - accessed via /db/getEmployees/ and /db/addEmployee/
urlpatterns = [
    path("getEmployees/", getEmployeeList, name="employee-list"),  # GET: returns JSON of all employees
    path("addEmployee/", addEmployee, name="add-employee"),  # GET: shows form, POST: saves employee
]

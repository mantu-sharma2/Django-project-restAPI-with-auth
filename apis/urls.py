# URL routing for apis app - accessed via /api/hello/, /api/home/, /api/add/
from django.contrib import admin
from django.urls import path
from apis.views import greet_view
from apis.views import home_page
from apis.views import add_numbers

# URL patterns - name parameter allows referencing in templates/redirects
urlpatterns= [
    path("hello/", greet_view, name="hello"), # Simple text response
    path("home/", home_page, name="home"),  # Template with context data
    path("add/", add_numbers, name="add")  # Calculator: GET=form, POST=result
]
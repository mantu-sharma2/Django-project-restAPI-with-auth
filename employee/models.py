from django.db import models

# Create your models here.

# Django Model - represents Employee table in database
# Django automatically creates database table with id, name, age, birthDate columns
class Employee(models.Model):
    name=models.CharField(max_length=100)  # Text field, max 100 chars
    age=models.IntegerField()  # Integer field for age
    birthDate=models.DateField()  # Date field for birth date
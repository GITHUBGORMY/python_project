from django.db import models

class student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    SId=models.CharField(max_length=10)
    Dob=models.CharField(max_length=10)

class Todo(models.Model):
    event=models.CharField(max_length=20)
    date=models.DateField()

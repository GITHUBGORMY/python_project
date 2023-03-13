from django.contrib import admin

# Register your models here.
from ToDoApp import models

admin.site.register(models.Todo)
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login (AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
class manager(models.Model):
     """customer = models.ForeignKey(Login, on_delete=models.CASCADE)"""
     username= models.CharField(max_length=200)
     Email = models.EmailField(max_length=200)
     address = models.CharField(max_length=200)
     phone = models.FloatField(max_length=200)


class worker(models.Model):
    """customer = models.ForeignKey(Login,on_delete=models.CASCADE)"""
    username = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.FloatField(max_length=200)


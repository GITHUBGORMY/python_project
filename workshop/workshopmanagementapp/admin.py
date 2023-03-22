from django.contrib import admin

# Register your models here.
from workshopmanagementapp import models

admin.site.register(models.Login)
admin.site.register(models.worker)
admin.site.register(models.manager)
from django.contrib import admin
from DataBase import models

# Register your models here.

admin.site.register(models.Tag)
admin.site.register(models.Question)
admin.site.register(models.Answers)
admin.site.register(models.Profile)
admin.site.register(models.User)
admin.site.register(models.Like)
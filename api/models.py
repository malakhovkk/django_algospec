from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
# class Person(models.Model):
#     # username = models.CharField(max_length=30)
#     # password = models.CharField(max_length=30)
#     # email = models.CharField(max_length=30)
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     paid = models.BooleanField(default=False)

# class Task(models.Model):
#     markdown = models.TextField(max_length=3000)
#     type = models.CharField(max_length=30)
#     difficulty = models.CharField(max_length=30)

# admin.site.register(Person)
# admin.site.register(Task)
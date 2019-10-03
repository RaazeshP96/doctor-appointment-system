from django.db import models
from django.contrib.auth.admin import User
from django.contrib.auth.models import AbstractUser


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    dob = models.DateField()
    specialization = models.CharField(max_length=30)
    qualification = models.FileField()

    def __str__(self):
        return self.name


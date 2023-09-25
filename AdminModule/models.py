from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USERS = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )

    user = models.CharField(choices=USERS, max_length=25, default='Admin')
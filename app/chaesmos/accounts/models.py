from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    created_time = models.DateTimeField(default=now)
    modified_time = models.DateTimeField(default=now)

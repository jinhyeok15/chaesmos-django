from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Account(AbstractUser):
    created_time = models.DateTimeField(default=now)
    modified_time = models.DateTimeField(default=now)

    first_name = None
    last_name = None

    class Meta:
        db_table = 'account'

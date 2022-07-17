from django.db import models

# commons
from commons.models import TimeStampedModel

# managers
from .managers import *

# settings
from chaesmos.settings import GENSALT_ROUND

# python utils
import uuid
import bcrypt

# Create your models here.


class UserAccount(TimeStampedModel):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    objects = UserAccountManager()

    def save(self, *args, **kwargs):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt(GENSALT_ROUND)).decode()
        super().save(*args, **kwargs)


class UserSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fk_user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    objects = UserSessionManager()

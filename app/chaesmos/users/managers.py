from django.db.models import Manager

# django exception
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# settings
from chaesmos.settings import USER_SESSION_EXPIRATION_DAYS

# django utils
from django.utils import timezone

# python utils
from datetime import timedelta
import bcrypt
from typing import Optional


class UserAccountManager(Manager):
    
    def login_user(self, username, password) -> Optional[object]:
        try:
            user = self.get(username=username)
        except ObjectDoesNotExist:
            return None
        hashed = user.password.encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed):
            return user
        return None


class UserSessionManager(Manager):

    def create(self, *args, expired_at=None, **kwargs):
        """
        override objects.create()
        """
        expired_at = timezone.now() + timedelta(days=USER_SESSION_EXPIRATION_DAYS)
        return super().create(*args, expired_at=expired_at, **kwargs)

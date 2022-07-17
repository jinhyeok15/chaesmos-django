from django.db.models import Manager

# django exception
from django.core.exceptions import ValidationError

# settings
from chaesmos.settings import USER_SESSION_EXPIRATION_DAYS

# python utils
from datetime import timedelta, datetime
import bcrypt
from typing import Optional, Type


class UserAccountManager(Manager):
    
    def login_user(self, username, password) -> Optional[object]:
        user = self.get(username=username)
        hashed = user.password.encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed):
            return user
        return None


class UserSessionManager(Manager):

    def create(self, *args, expired_at=None, **kwargs):
        """
        override objects.create()
        """
        expired_at = datetime.now() + timedelta(days=USER_SESSION_EXPIRATION_DAYS)
        return super().create(*args, expired_at=expired_at, **kwargs)

from django.db.models import Manager

# django exception
from django.core.exceptions import ValidationError, ObjectDoesNotExist

# settings
from chaesmos.settings import USER_SESSION_EXPIRATION_DAYS, GENSALT_ROUND

# django utils
from django.utils import timezone

# python utils
from datetime import timedelta
import bcrypt
from typing import Optional

__all__ = [
    'UserAccountManager',
    'UserSessionManager',
]


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

    def get_or_none(self, id):
        if id is None:
            return None
        try:
            session = self.get(pk=id)
            return session
        except ObjectDoesNotExist:
            return None
    
    def is_valid(self, id):
        obj = self.get_or_none(id)
        if obj is None:
            return False
        if obj.expired_at < timezone.now():
            return False
        return True

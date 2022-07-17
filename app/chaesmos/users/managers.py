from django.db.models import Manager

# settings
from chaesmos.settings import USER_SESSION_EXPIRATION_DAYS

# python utils
from datetime import timedelta, datetime


class UserAccountManager(Manager):
    pass


class UserSessionManager(Manager):

    def create(self, *args, expired_at=None, **kwargs):
        """
        override objects.create()
        """
        expired_at = datetime.now() + timedelta(days=USER_SESSION_EXPIRATION_DAYS)
        return super().create(*args, expired_at=expired_at, **kwargs)

from django.test import TestCase

from django.utils import timezone
from datetime import timedelta

from .models import UserAccount, UserSession

# Create your tests here.


def user_factory(size):
    factory_data = []

    for i in range(size):
        factory_data.append(UserAccount.objects.create(
            username=f'user{i}',
            password=f'password{i}',
            nickname=f'nickname{i}'
        ))

    return factory_data


class UserSessionTestCase(TestCase):
    def setUp(self):
        self.user_data = user_factory(3)

    def test_session_expired(self):
        session = UserSession.objects.create(fk_user_account=self.user_data[0])

        self.assertTrue(UserSession.objects.is_valid(session.id))

        session.expired_at = timezone.now() - timedelta(days=1)
        session.save()
        
        self.assertFalse(UserSession.objects.is_valid(session.id))

from django.db import models, transaction
from django.conf import settings

# utils
from datetime import datetime, timedelta
from datetime import date
import random
from django.utils import timezone


class LetterManager(models.Manager):
    def rand_read(self, user) -> list:
        size = settings.MAX_DAILY_LETTER_COUNT

        end_dt = datetime.now()
        start_dt = end_dt - timedelta(days=7)
        qs = self.filter(created_at__range=(start_dt, end_dt))\
                .exclude(fk_writer=user).exclude(solutions__fk_sender=user)
        
        if len(qs) >= size:
            return random.sample(list(qs), size)
        else:
            end_dt = datetime.now()
            start_dt = end_dt - timedelta(days=30)

            for i in range(settings.MAX_READ_COUNT):
                start_dt -= timedelta(days=30*i)
                qs = self.filter(created_at__range=(start_dt, end_dt)).exclude(fk_writer=user).exclude(solutions__fk_sender=user)

                if len(qs) >= size:
                    return random.sample(list(qs), size)
        if qs:
            return random.sample(list(qs), len(qs))

        return []


class DailyPostManager(models.Manager):
    def generate(self, user, letters) -> None:
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_datetime = datetime.fromordinal(tomorrow.toordinal())
        with transaction.atomic():
            for letter in letters:
                super().create(fk_letter=letter, fk_reader=user, expired_at=tomorrow_datetime)

    def is_expired(self, user):
        post = self.filter(fk_reader=user).last()  # 확실하게 일자별로 descending sort해주고 first()로 불러오는 것이 더 좋을 듯

        if not post:
            return True
        
        if post.expired_at <= timezone.now():
            return True
        
        return False

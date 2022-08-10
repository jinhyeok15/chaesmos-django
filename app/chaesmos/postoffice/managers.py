from django.db import models, transaction
from django.conf import settings

# utils
from datetime import datetime, timedelta
from datetime import date
import random


class LetterManager(models.Manager):
    def rand_read(self):
        size = settings.MAX_DAILY_LETTER_COUNT

        end_dt = datetime.now()
        start_dt = end_dt - timedelta(days=7)
        qs = self.filter(created_at__range=(start_dt, end_dt))
        
        if len(qs) >= size:
            return random.sample(qs, size)
        else:
            end_dt = datetime.now()
            start_dt = end_dt - timedelta(days=30)

            for i in range(settings.MAX_READ_COUNT):
                start_dt -= timedelta(days=30*i)
                qs = self.filter(created_at__range=(start_dt, end_dt))

                if len(qs) >= size:
                    return random.sample(qs, size)
        return random.sample(self.all(), size)


class DailyPostManager(models.Manager):
    def generate(self, user, letters) -> None:
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_datetime = datetime.fromordinal(tomorrow.toordinal())
        with transaction.atomic():
            for letter in letters:
                super().create(fk_letter=letter, fk_reader=user, expired_at=tomorrow_datetime)

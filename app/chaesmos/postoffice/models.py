from django.db import models

# commons
from commons.models import TimeStampedModel

# other models
from users.models import UserAccount

# managers
from .managers import *

# Create your models here.


class Letter(TimeStampedModel):
    fk_writer = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='letters')
    title = models.CharField(max_length=50)
    main = models.TextField()
    selected_date = models.DateField()

    objects = LetterManager()


class Tag(models.Model):
    fk_letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=10)


class Solution(TimeStampedModel):
    fk_letter = models.ForeignKey(Letter, on_delete=models.SET_NULL, null=True, related_name='solutions')
    fk_sender = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, related_name='senders')
    main = models.TextField()


class DailyPost(models.Model):
    fk_letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    fk_reader = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='dailyposts')
    expired_at = models.DateTimeField()

    objects = DailyPostManager()

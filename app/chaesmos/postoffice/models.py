from django.db import models
from commons.models import TimeStampedModel
from users.models import UserAccount

# Create your models here.


class Letter(TimeStampedModel):
    fk_writer = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='letters')
    title = models.CharField(max_length=50)
    main = models.TextField()
    selected_date = models.DateField()


class Tag(models.Model):
    fk_letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=10)


class Solution(TimeStampedModel):
    fk_letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='solutions')
    fk_sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='senders')
    main = models.TextField()

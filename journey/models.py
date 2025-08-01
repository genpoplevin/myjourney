from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Journey(models.Model):
    location = models.CharField(max_length=250)
    cost = models.IntegerField()
    heritage = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='journeys'
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Journey(models.Model):
    location = models.CharField(max_length=250)
    cost = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='journeys'
    )
    created = models.DateTimeField(auto_now_add=True)


class Place(models.Model):
    journey = models.ForeignKey(
        Journey,
        related_name='places',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)

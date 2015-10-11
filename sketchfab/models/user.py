from sketchfab.models.badge import Badge

from django.db import models
from django.utils import timezone


class User(models.Model):
    """ A basic user class. """
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_created = models.DateField(default=timezone.now)
    badges = models.ManyToManyField(Badge, through='Milestone')

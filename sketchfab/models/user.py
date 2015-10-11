from rest_framework import serializers

from sketchfab.models.badge import Badge

from django.db import models
from django.utils import timezone


class User(models.Model):
    """ A basic user class. """
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateField(default=timezone.now)
    badges = models.ManyToManyField(Badge, through='Milestone')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ UserSerializer is used to serialize data for the REST API endpoint. """
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'badges')

from rest_framework import serializers

from django.db import models


class Badge(models.Model):
    """ A class representing the badges a user can win. """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    """ BadgeSerializer serializes data for the REST API endpoint. """
    class Meta:
        model = Badge
        fields = ('name', 'description')

from rest_framework import serializers

from django.db import models


class Badge(models.Model):
    """ A class representing the badges a user can win.

        So far, badges are:

        Collector
            Upload 5 or more models.
        Newcomer
            Join the Sketchfab community..
        Pionneer
            1 year since joining Sketchfab.
        Star
            Reach 1k views on one of your models..
        VIP
            Mysteriously given to a few chosen members.
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    """ BadgeSerializer serializes data for the REST API endpoint. """
    class Meta:
        model = Badge
        fields = ('name', 'description')

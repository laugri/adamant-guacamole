from rest_framework import serializers

from sketchfab.models.user import User

from django.db import models
from django.utils import timezone


class Model3D(models.Model):
    """ A class representing a 3D model. """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_created = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Model3DSerializer(serializers.HyperlinkedModelSerializer):
    """ Model3DSerializer serializes data for the REST API endpoint. """
    class Meta:
        model = Model3D
        fields = ('name',
                  'description',
                  'date_created',
                  'user')

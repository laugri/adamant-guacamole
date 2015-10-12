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

    def seniority(self):
        """ Returns the seniority of the member in days. """
        return (timezone.now().date() - self.date_joined).days

    def models(self):
        """ Returns the user's 3D models. """
        from sketchfab.models.model3d import Model3D
        return Model3D.objects.filter(user=self)

    def number_of_models(self):
        """ Returns the number of 3D models a user has. """
        return len(self.models())

    def achievements(self):
        """ Gets the user's achievements.
            Returns:
                A list of the user's badge names.
        """
        return [badge.name for badge in self.badges.all()]


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

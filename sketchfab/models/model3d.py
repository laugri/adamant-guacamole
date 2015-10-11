from sketchfab.models.user import User

from django.db import models
from django.utils import timezone


class Model3D(models.Model):
    """ A class representing a 3D model. """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date_created = models.DateField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

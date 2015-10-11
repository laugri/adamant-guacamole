from django.db import models


class Badge(models.Model):
    """ A class representing the badges a user can win. """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

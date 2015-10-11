from sketchfab.models.badge import Badge
from sketchfab.models.user import User

from django.db import models
from django.utils import timezone


class Milestone(models.Model):
    """ A milestone holds data about the badge a particular user got.

    Milestones are used to store extra information on the many-to-many
    relationship between Users and Badges, following [this Django pattern]
    (https://docs.djangoproject.com/en/1.8/topics/db/models/#extra-fields-on-many-to-many-relationships)

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date_obtained = models.DateField(default=timezone.now)

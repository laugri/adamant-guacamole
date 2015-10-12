""" All Sketchfab signals are listed here. """

from sketchfab.models.badgemanager import BadgeManager
from sketchfab.models.user import User, UserSerializer
from sketchfab.models.model3d import Model3D, Model3DSerializer

from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def update_user_badges(sender, **kwargs):
    """ Receiver checking new achievements for a user.
        Arbitrary triggered on User save() to demonstarte the idea.
    """
    print('Signal received from User save()!')
    user = kwargs['instance']
    badgemanager = BadgeManager(user)
    badgemanager.attribute_milestones()
    return None

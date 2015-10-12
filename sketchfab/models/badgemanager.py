from sketchfab.models.badge import Badge
from sketchfab.models.user import User
from sketchfab.models.milestone import Milestone


class BadgeManager(object):
    """ BadgeManager's purpose is to attribute badges to users.

        BadgeManager checks achievements made by a user and attributes
        the correct badges via milestones.

        Returns:
            achievements (List[Str]): the list of badge names corresponding
                to the user's achievements.
    """
    def __init__(self, user):
        self.user = user

    def check_achievements(self):
        """ This method checks the user's achievements and lists them. """
        achievements = ['Newcomer']

        if self.user.number_of_models() >= 5:
            achievements.append('Collector')

        if self.user.seniority() >= 365:
            achievements.append('Pionneer')

        user_models = self.user.models()
        if (user_models and
                max(user_models, key=lambda x: x.views).views > 1000):
            achievements.append('Star')

        return achievements

    def attribute_milestones(self):
        """ Gives milestones to a user according to its achievements. """
        achievements = self.check_achievements()
        for achievement in achievements:
            # Check that the user does not already have this bagde.
            if achievement in self.user.achievements():
                # If so, skip the achievement.
                continue
            badge = Badge.objects.get(name=achievement)
            Milestone(user=self.user, badge=badge).save()
        return None

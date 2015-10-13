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

    def is_collector(self):
        return self.user.number_of_models() >= 5

    def is_pionneer(self):
        return self.user.seniority() >= 365

    def is_star(self):
        user_models = self.user.models()
        return (user_models and
                max(user_models, key=lambda x: x.views).views > 1000)

    def check_achievements(self):
        """ This method checks the user's achievements and lists them. """
        achievements = ['Newcomer']

        if self.is_collector():
            achievements.append('Collector')

        if self.is_pionneer():
            achievements.append('Pionneer')

        if self.is_star():
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

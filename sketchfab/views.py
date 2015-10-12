from rest_framework import viewsets

from sketchfab.models.badge import Badge, BadgeSerializer
from sketchfab.models.model3d import Model3D, Model3DSerializer
from sketchfab.models.user import User, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class Model3DViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Model3Ds to be viewed or edited."""
    queryset = Model3D.objects.all().order_by('-date_created')
    serializer_class = Model3DSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Badges to be viewed or edited."""
    queryset = Badge.objects.all().order_by('name')
    serializer_class = BadgeSerializer

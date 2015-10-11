"""sketchfab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/

For the API, see: http://www.django-rest-framework.org/api-guide/routers/
"""

from sketchfab import views

from rest_framework import routers

from django.conf.urls import include, url
from django.contrib import admin


# Wire up our API using automatic URL routing.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'model3ds', views.Model3DViewSet)
router.register(r'badges', views.BadgeViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
]

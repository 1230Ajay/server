from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Contents',contentsViewSet )
router.register(r'Service',servicesViewSet)
router.register(r'Profile',profileViewSet)
router.register(r'Education',educationViewSet)
router.register(r'Experience',ExperienceViewSet)


urlpatterns = [
    path('',include(router.urls))
]
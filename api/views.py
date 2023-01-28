
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class contentsViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = contentsSerializer


class servicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = serviceSerializer

class profileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class educationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperieanceSerializer
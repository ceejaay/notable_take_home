from django.shortcuts import render
from shiren.models import Swords
from rest_framework import viewsets
from .serializers import SwordSerializer

class SwordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Swords.objects.all()
    serializer_class = SwordSerializer



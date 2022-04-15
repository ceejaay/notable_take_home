from django.shortcuts import render
from shiren.models import Prices, Scrolls
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import PriceSerializer, ScrollSerializer

# class SwordViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = Swords.objects.all()
#     serializer_class = SwordSerializer


# class PriceViewSet(viewsets.ModelViewSet):
#     queryset = Prices.objects.all()
#     serializer_class = PriceSerializer

@csrf_exempt
def prices(request):
    return JsonResponse({"prices": "all the prices"})

@csrf_exempt
def scrolls(request):
    return JsonResponse({"scrolls": "all the scrolls"})

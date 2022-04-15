from shiren.models import Swords, Scrolls, Prices
from rest_framework import serializers


class SwordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Swords
        fields = ['name', 'type']

class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prices
        fields = ['price']

class ScrollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scrolls 
        fields = ['price']

from shiren.models import Swords
from rest_framework import serializers


class SwordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Swords
        fields = ['name', 'type']


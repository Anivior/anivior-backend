from rest_framework import serializers
from .models import SOS


class LocateNgo(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = SOS
        fields = ['category', 'image', 'longitude', 'latitude']
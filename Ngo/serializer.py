from .models import NGO
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class NgoSerializer(ModelSerializer):

    class Meta:
        model = NGO
        fields = ['name', 'email', 'city', 'pincode', 'contact', 'point']



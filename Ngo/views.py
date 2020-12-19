from django.contrib import auth
from rest_framework.generics import GenericAPIView
from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from .serializer import *
from rest_framework.permissions import AllowAny


class ResgisterView(GenericAPIView):
    serializer_class = NgoSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        farmer_data = request.data
        serializer = self.serializer_class(data=farmer_data)

        if not serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_keys) > 0 and len(error_values) > 0:
                response_data = {f'{error_keys[0]}': f'{error_values[0][0]}'}
                return response.Response(response_data, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response_data = {"Success": "Farmer added successfully"}
        return response.Response(response_data, status.HTTP_201_CREATED)
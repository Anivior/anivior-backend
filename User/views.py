from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.response import Response
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from Ngo.models import NGO
from Ngo.serializer import NgoSerializer
# Create your views here.


class LocateNgo(GenericAPIView):
    serializer_class = LocateNgo
    queryset = NGO

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            error_values = list(serializer.errors.values())
            error_keys = list(serializer.errors.keys())
            if len(error_values) > 0 and len(error_keys) > 0:
                return Response(f'{error_keys[0]}: {error_values[0][0]}', status.HTTP_200_OK)

        latitude = float(serializer.data['latitude'])
        longitude = float(serializer.data['longitude'])

        location = GEOSGeometry(f'POINT({longitude} {latitude})', srid=4326)
        Ngo_within_radius = NGO.objects.filter(point__distance_lte = (location, D(km=5)))

        serializer = NgoSerializer(Ngo_within_radius, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
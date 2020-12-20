from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.response import Response
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry
from Ngo.models import NGO
from Ngo.serializer import NgoSerializer
from Anivior_backend import settings
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

        sos = serializer.save()
        print(sos.category)
        print(sos.latitude)
        print(sos.longitude)
        print(sos.image.url)

        latitude = float(serializer.data['latitude'])
        longitude = float(serializer.data['longitude'])
        image = sos.image
        # category = serializer.data['category']
        
        img_data = image.read()
        html_part = MIMEMultipart(_subtype='related')
        body = MIMEText('<p>Hello <img src="cid:myimage" /></p>', _subtype='html')
        html_part.attach(body)
        
        img = MIMEImage(img_data, 'jpeg')
        img.add_header('Content-Id', '<myimage>')
        img.add_header("Content-Disposition", "inline", filename="myimage")
        html_part.attach(img)

        from_email = settings.EMAIL_HOST_USER
        recipient_list = ["201951083@iiitvadodara.ac.in", ]
        msg = EmailMessage('Subject Line', None, from_email, recipient_list)
        msg.attach(html_part)
        msg.send()
        location = GEOSGeometry(f'POINT({longitude} {latitude})', srid=4326)
        Ngo_within_radius = NGO.objects.filter(point__distance_lte = (location, D(km=5)))

        serializer = NgoSerializer(Ngo_within_radius, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
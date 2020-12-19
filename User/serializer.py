from rest_framework import serializers


class LocateNgo(serializers.Serializer):
    latitude = serializers.DecimalField(max_digits=16, decimal_places=6, default=0.0)
    longitude = serializers.DecimalField(max_digits=16, decimal_places=6, default=0.0)

    class Meta:
        fields = ['latitude', 'longitude']


    def validate(self, attrs):
        latitude = attrs.get('latitude')
        longitude = attrs.get('longitude')

        if not latitude or not longitude:
            raise TypeError('Location fields can not be empty')
        return super().validate(attrs)
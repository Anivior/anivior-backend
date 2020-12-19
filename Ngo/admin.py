from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import NGO
# Register your models here.


admin.site.register(NGO, LeafletGeoAdmin)
from django.urls import path
from .views import LocateNgo

urlpatterns = [
    path('help/', LocateNgo.as_view(), name='help')
]

from django.urls import path
from .views import ResgisterView

urlpatterns = [
    path('register/', ResgisterView.as_view(), name='register')
]
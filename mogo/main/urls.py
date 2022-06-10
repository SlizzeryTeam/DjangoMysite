from django.urls import path, include
from .views import *
from main.views import index

urlpatterns = [
    path('', index)
]

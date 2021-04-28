from django.urls import path
from core.views import index, about

urlpatterns = [
    path('', index),
    path('about', about),
]

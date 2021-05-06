from django.urls import path
from core.views import index, about, collection, product, test

urlpatterns = [
    path('', index),
    path('about', about),
    path('collection', collection),
    path('product/<int:product_id>', product, name="product"),
    path('test', test)
]

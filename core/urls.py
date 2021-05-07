from django.urls import path
from core.views import index, about, collection, product

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('collection', collection, name="collection"),
    path('product/<int:product_id>', product, name="product"),
]

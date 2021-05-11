from django.urls import path
from core.views import index, about, collection, product, register_product

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('collection', collection, name="collection"),
    path('product/<int:product_id>', product, name="product"),
    path('product/register', register_product, name="register product")
]

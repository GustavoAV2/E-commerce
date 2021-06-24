from django.urls import path
from core.views import about, collection, product, manager_historic, payment_product, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('about', about, name="about"),
    # path('collection', collection, name="collection"),
    path('product/<int:product_id>', product, name="product"),
    # path('manager/historic', manager_historic, name="manager historic"),
    # path('payment/<int:product_id>', payment_product, name="payment_product")
]

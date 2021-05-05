from django.shortcuts import render
from core.models import Product


def index(request):
    products = Product.objects.all()
    last_number = 9 if len(products) > 9 else len(products)

    context = {
        "products": products[0:last_number],
        "new": {
            "name": products[0].name.split(' '),
            "price": products[0].price
        }
    }
    return render(request, "index.html", context)


def collection(request, pag: int = 1):
    products = Product.objects.all()
    first_number = 0 if pag == 0 else (pag - 1) * 9
    last_number = pag * 9

    list_products = products[first_number:last_number]

    context = {
        "products": list_products,
    }
    return render(request, "store.html", context)


def product(request, product_id: int):
    product_selected = Product.objects.get(id=product_id)
    context = {
        "product": product_selected
    }
    return render(request, "product.html", context)


def test(request):
    return render(request, "racing_boots.html")


def about(request):
    return render(request, "about.html")

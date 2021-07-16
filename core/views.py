from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from core.models import Product, Info
from .forms import ContactForm, ProductModelForm
from mp_functions.functions import create_preference


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        products = Product.objects.all()
        info = Info.objects.all()
        last_number = 9 if len(products) > 9 else len(products)

        context = {}
        if products:
            context.update({
                "contact": info,
                "products": products[0:last_number],
                "new": {
                    "id": products[0].id,
                    "image": products[0].image,
                    "name": products[0].name.split(' '),
                    "price": products[0].price
                }
            })
        return render(request, self.template_name, context)


def collection(request, pag: int = 1):
    products = Product.objects.all()
    info = Info.objects.all()

    first_number = 0 if pag == 0 else (pag - 1) * 9
    last_number = pag * 9

    list_products = products[first_number:last_number]

    context = {
        "products": list_products,
        "contact": info,
    }

    return render(request, "store.html", context)


def product(request, product_id: int):
    product_selected = get_object_or_404(Product, id=product_id)
    info = Info.objects.all()

    context = {
        "product": product_selected,
        "catalog": True,
        "sizes": [size for size in range(1, product_selected.amount)],
        "contact": info
    }
    return render(request, "product.html", context)


def manager_historic(request):
    if str(request.user) != "AnonymousUser":
        if str(request.method) == "POST":
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Produto salvo com sucesso!")
            else:
                messages.error(request, "Erro ao salvar produto!")
        else:
            form = ProductModelForm()
        context = {"form": form}
        return render(request, "register_product.html", context)
    return redirect(to="/")


def payment_product(request, product_id: int, amount: int = 1):
    product_selected = get_object_or_404(Product, id=product_id)
    if product_selected:
        product_dictionary = product_selected.serialize()
        url_payment = create_preference(product_dictionary=product_dictionary, amount=amount)
        print(url_payment)
        return redirect(url_payment, permanent=True)


def about(request):
    form = ContactForm(request.POST or None)
    if str(request.method) == "POST":
        if form.is_valid():
            form.send_email()
            messages.success(request, "E-mail enviado com sucesso!")
            form = ContactForm()
        else:
            messages.error(request, "Erro ao enviar email! Tente novamente mais tarde...")

    context = {
        "form": form
    }
    info = Info.objects.all()
    context.update({"contact": info})
    return render(request, "contact.html", context)


#  Last form to coding errors
"""
    from django.http import HttpResponse
    from django.template import loader
    
    def error404(request, exception):
        template = loader.get_template("errors/404.html")
        return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)
    
    
    def error500(request):
        template = loader.get_template("errors/500.html")
        return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
"""

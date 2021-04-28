from django.shortcuts import render


def index(request):
    context = {
        "user": "Gustavo"
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")

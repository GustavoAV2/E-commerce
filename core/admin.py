from django.contrib import admin
from .models import Product, Info


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount", "slug", "creation_date", "active")


@admin.register(Info)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("service", "creation_date", "active")

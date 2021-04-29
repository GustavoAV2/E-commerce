from django.contrib import admin
from .models import User, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount")


admin.site.register(User)
admin.site.register(Product, ProductAdmin)

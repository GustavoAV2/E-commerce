from django.contrib import admin
from .models import User, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount", "slug", "creation_date", "active")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "creation_date", "active")


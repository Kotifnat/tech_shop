from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Product, Image
# Register your models here.


class ImageInline(TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Product, Image, Tag
# Register your models here.


class ImageInline(TabularInline):
    model = Image
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
admin.site.register(Tag)

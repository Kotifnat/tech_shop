from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Image
# Create your views here.


class ProductListView(ListView):
    model = Product
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.all()

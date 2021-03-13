from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    SmartphoneSerializer,
    NotebookSerializer,
)
from products.models import Category, Smartphone, Notebook, Product


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class NotebookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']

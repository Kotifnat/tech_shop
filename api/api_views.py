from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


from .serializers import (
    CategorySerializer,
    SmartphoneSerializer,
    NotebookSerializer,
)
from products.models import Category, Smartphone, Notebook


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
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


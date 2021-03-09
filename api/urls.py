from django.urls import path, include

from rest_framework.routers import SimpleRouter
from .api_views import (
    CategoryListCreateAPIView,
    SmartphoneViewSet,
    NotebookViewSet,
)

router = SimpleRouter()
router.register('smartphones', SmartphoneViewSet, basename='smartphones')
router.register('notebooks', NotebookViewSet, basename='notebooks')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateAPIView.as_view(), name='categories'),
]

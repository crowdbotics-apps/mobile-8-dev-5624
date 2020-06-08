from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HgjkhglkjViewSet

router = DefaultRouter()
router.register("hgjkhglkj", HgjkhglkjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

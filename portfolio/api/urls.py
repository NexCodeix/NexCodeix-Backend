from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("portfolio", views.PortfolioModelViewSet, basename="portfolio")

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DomainModelViewSet, ContactUsModelViewSet

router = DefaultRouter()
router.register("domain", DomainModelViewSet,basename="domain")
router.register("contact-us", ContactUsModelViewSet,basename="contact-us")

urlpatterns = [
    path("", include(router.urls)),
] 

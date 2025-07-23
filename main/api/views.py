from rest_framework.viewsets import ModelViewSet
from ..models import Domain, ContactUs
from .serializers import DomainSerializer, ContactUsSerializer


class DomainModelViewSet(ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class ContactUsModelViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

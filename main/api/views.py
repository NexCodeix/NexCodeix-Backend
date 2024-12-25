from rest_framework.viewsets import ModelViewSet
from .serializers import PortfolioDetailSerializer, PortfolioSerializer


class PortfolioModelViewSet(ModelViewSet):
    default_serializer_class = PortfolioSerializer
    actions_serializer_class = {
        "detail": PortfolioDetailSerializer,
    }

    def get_queryset(self):
        qs = Portfolio.objects.all()
        return qs

    def get_serializer_class(self):
        if self.actions_serializer_class.get(self.action, None):
            serializer = self.actions_serializer_class[self.action]
            return serializer
        
        return self.default_serializer_class


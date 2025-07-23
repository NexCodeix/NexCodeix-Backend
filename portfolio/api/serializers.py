from ..models import Portfolio, PortfolioContent, PortfolioImage
from rest_framework import serializers


class PortfolioContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioContent
        fields = "__all__"


class PortfolioImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioImage
        fields = "__all__"


class PortfolioSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Portfolio
        fields = "__all__"


class PortfolioDetailSerializer(serializers.ModelSerializer):
    contents = PortfolioContentSerializer(
        read_only=True,
        many=True,

    )
    images = PortfolioImageSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Portfolio
        fields = "__all__"

from rest_framework import serializers
from ..models import Domain, ContactUs


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = "__all__"

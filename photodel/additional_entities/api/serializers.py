from additional_entities.models import Country
from rest_framework import serializers


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['name_country', ]
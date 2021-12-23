from additional_entities.models import Country, Language
from rest_framework import serializers


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['name_country', ]


class LanguageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['name_language', ]
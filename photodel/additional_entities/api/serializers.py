from additional_entities.models import Country, Language, Advertisement
from rest_framework import serializers


class CountryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name_country', ]


class LanguageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['id', 'name_language', ]


class AdvertisementListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ['id', 'ad_image', 'ad_title', 'ad_link', 'ad_count_click', ]


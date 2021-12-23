from rest_framework import viewsets, status
from additional_entities.models import Country, Language
from .serializers import CountryListSerializer, LanguageListSerializer
from rest_framework.response import Response


class CountryViewSet(viewsets.ViewSet):
    def list_country(self, request):
        queryset = Country.objects.all()
        serializer = CountryListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class LanguageViewSet(viewsets.ViewSet):
    def list_language(self, request):
        queryset = Language.objects.all()
        serializer = LanguageListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


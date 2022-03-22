from rest_framework import viewsets, status
from additional_entities.models import Country, Language, Advertisement
from film_places.models import FilmPlacesComment
from gallery.models import GalleryComment, PhotoSessionComment
from .serializers import CountryListSerializer, LanguageListSerializer, AdvertisementListSerializer
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


class AdvertisementViewSet(viewsets.ViewSet):

    def list_advertisement(self, request):
        queryset = Advertisement.objects.all()
        serializer = AdvertisementListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def add_click_to_advertisement(self, request, pk):
        queryset = Advertisement.objects.get(id=pk)
        queryset.ad_count_click += 1
        queryset.save()
        return Response(status=status.HTTP_200_OK)


class CommonViewSet(viewsets.ViewSet):

    def list_last_comments(self, request):
        photo_comment = GalleryComment.objects.last().value('content', 'timestamp', 'sender_comment__name')
        photo_session_comment = PhotoSessionComment.objects.last()
        place_comment = FilmPlacesComment.objects.last()
        print(photo_comment)
        return Response(status=status.HTTP_200_OK)


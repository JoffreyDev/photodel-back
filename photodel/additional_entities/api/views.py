from rest_framework import viewsets, status
from additional_entities.models import Country, Language, Advertisement, City
from film_places.models import FilmPlacesComment
from gallery.models import GalleryComment, PhotoSessionComment
from .serializers import CountryListSerializer, LanguageListSerializer, \
    AdvertisementListSerializer, CityListSerializer
from rest_framework.response import Response
from services.additional_service import check_town_use_coords


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


class CityViewSet(viewsets.ViewSet):
    def list_city(self, request):
        queryset = City.objects.all()
        serializer = CityListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def check_coordinates(self, request):
        queryset = City.objects.all()
        nearest_city = check_town_use_coords(queryset, request.GET.get('user_coordinates', ''))
        serializer = CityListSerializer(nearest_city)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CommonViewSet(viewsets.ViewSet):

    def list_last_comments(self, request):
        photo_comment = {'photo_comment':
                         GalleryComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                       'sender_comment__surname', 'sender_comment__status',
                                                       'gallery__name_image').last()
                         }

        photo_comment.update({'photo_session_comment':
                              PhotoSessionComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                                 'sender_comment__surname', 'sender_comment__status',
                                                                 'photo_session__session_name').last()
                              })
        photo_comment.update({'place_comment':
                              FilmPlacesComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                               'sender_comment__surname', 'sender_comment__status',
                                                               'place__name_place').last()
                              })
        return Response(status=status.HTTP_200_OK, data=photo_comment)


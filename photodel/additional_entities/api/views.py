from threading import currentThread
from rest_framework import viewsets, status, permissions
from additional_entities.models import Country, Language, Advertisement, City, Question
from film_places.models import FilmPlacesComment
from gallery.models import GalleryComment, PhotoSessionComment
from accounts.models import Profile
from additional_entities.models import CustomSettings
from .serializers import CountryListSerializer, LanguageListSerializer, \
    AdvertisementListSerializer, CityListSerializer, AnswerCreateSerializer, \
    QuestionListSerializer, AdChangeSerializer
from rest_framework.response import Response
from services.additional_service import check_town_use_coords, check_exitst_answer
import datetime
import math


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
        current_adv = CustomSettings.objects.all().first().current_ad
        queryset = Advertisement.objects.get(pk=current_adv)
        serializer = AdvertisementListSerializer(queryset)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def add_click_to_advertisement(self, request, pk):
        try:
            queryset = Advertisement.objects.get(id=pk)
            queryset.ad_count_click += 1
            queryset.save()
            return Response(status=status.HTTP_200_OK)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # def task_update_current_ad():

    #     current_ad = CustomSettings.objects.all().first().current_ad
    #     if Advertisement.objects.all().count() == current_ad:
    #         current_ad = 1
    #     else:
    #         current_ad += 1
    #     current_ad.save()


class CityViewSet(viewsets.ViewSet):
    def list_city(self, request):
        queryset = City.objects.all()
        serializer = CityListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def check_coordinates(self, request):
        queryset = City.objects.all()
        nearest_city = check_town_use_coords(
            queryset, request.GET.get('user_coordinates', ''))
        serializer = CityListSerializer(nearest_city)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PollViewSet(viewsets.ViewSet):
    permission_classes_by_action = {
        'add_answer': [permissions.IsAuthenticated, ],
    }

    def list_poll(self, request):
        queryset = Question.objects.filter(is_hide=False)
        serializer = QuestionListSerializer(
            queryset, many=True, context={'user': request.user})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def add_answer(self, request):
        profile = Profile.objects.get(user=request.user).id
        serializer = AnswerCreateSerializer(
            data=request.data | {"profile": profile})
        serializer.is_valid(raise_exception=True)
        if check_exitst_answer(request.user, request.data.get('choice')):
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"message": "Вы уже оставляли ответ в этом опросе"})
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CommonViewSet(viewsets.ViewSet):

    def list_last_comments(self, request):
        photo_comment = {'photo_comment':
                         GalleryComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                       'sender_comment__surname', 'sender_comment__status',
                                                       'gallery__name_image', 'sender_comment__id', 'gallery__id', 'sender_comment__user_channel_name').last()
                         }

        photo_comment.update({'photo_session_comment':
                              PhotoSessionComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                                 'sender_comment__surname', 'sender_comment__status',
                                                                 'photo_session__session_name', 'sender_comment__id', 'photo_session__id', 'sender_comment__user_channel_name').last()
                              })
        photo_comment.update({'place_comment':
                              FilmPlacesComment.objects.values('content', 'timestamp', 'sender_comment__name',
                                                               'sender_comment__surname', 'sender_comment__status',
                                                               'place__name_place', 'sender_comment__id', 'place__id', 'sender_comment__user_channel_name').last()
                              })
        return Response(status=status.HTTP_200_OK, data=photo_comment)

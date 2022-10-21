from django.contrib.auth.models import AnonymousUser
from django.db.models import Count, F, Subquery, Func, OuterRef

from rest_framework import serializers

from additional_entities.models import (
    Country,
    Language,
    Advertisement,
    City,
    Question,
    Choice,
    Answer,
)
from additional_entities.models import CustomSettings


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
        fields = ['id', 'ad_image', 'ad_title',
                  'ad_link']


class CityListSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()

    class Meta:
        model = City
        fields = ['city_name', 'coordinates', 'country', ]


class ChoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['title', 'id']


class QuestionListSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    count_answer = serializers.SerializerMethodField()
    is_vote = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['title', 'is_hide', 'choices', 'count_answer', 'is_vote', ]

    def get_choices(self, obj):
        answers = Answer.objects.filter(
            choice=OuterRef("id")
        ).order_by().annotate(
            count=Func(F('id'), function='Count')
        ).values('count')
        choices = Choice.objects.filter(
            question__id=obj.id
        ).values('title', 'id').annotate(total=Subquery(answers))
        return choices

    def get_count_answer(self, obj):
        return Answer.objects.filter(choice__question=obj.id).count()

    def get_is_vote(self, obj):
        if isinstance(self.context.get('user'), AnonymousUser):
            return ''
        return Answer.objects.filter(choice__question=obj.id, profile__user=self.context.get('user')).exists()


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AdChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomSettings
        fields = ['current_ad']

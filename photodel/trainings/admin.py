from django.contrib import admin
from trainings.models import Trainings, TrainingsComment, TrainingsFavorite, TrainingsLike, TrainingCategory, TrainingsRequest


@admin.register(Trainings)
class TrainingsAdmin(admin.ModelAdmin):
    list_display = ['training_title', 'start_date', 'start_date']


@admin.register(TrainingsComment)
class TrainingsCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'sender_comment', 'training', ]


@admin.register(TrainingsFavorite)
class TrainingsFavoriteAdmin(admin.ModelAdmin):
    list_display = ['profile', 'training', ]


@admin.register(TrainingsLike)
class TrainingsLikeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'training', ]


@admin.register(TrainingCategory)
class TrainingsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]


@admin.register(TrainingsRequest)
class TrainingsRequestAdmin(admin.ModelAdmin):
    list_display = ['training', ]

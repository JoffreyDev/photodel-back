from django.contrib import admin
from .models import Profile, VerificationCode, ProCategory, Specialization, \
    ProfileComment, ProfileLike, ProfileFavorite, TeamInvites, Notifications, Payment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email',
                    'phone', 'status', 'last_ip', 'id', ]
    
@admin.register(Payment)
class ProfilePayment(admin.ModelAdmin):
    list_display = ['account']



@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'email_code', ]


@admin.register(ProCategory)
class ProCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category', ]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name_spec', ]


@admin.register(ProfileComment)
class ProfileCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp',
                    'sender_comment', 'receiver_comment', ]


@admin.register(ProfileLike)
class ProfileLikeAdmin(admin.ModelAdmin):
    list_display = ['sender_like', 'receiver_like', ]


@admin.register(ProfileFavorite)
class ProfileFavoriteAdmin(admin.ModelAdmin):
    list_display = ['sender_favorite', 'receiver_favorite', ]


@admin.register(TeamInvites)
class TeamInvites(admin.ModelAdmin):
    list_display = ['invite_sender', 'invite_receiver']


@admin.register(Notifications)
class Notifications(admin.ModelAdmin):
    list_display = ['sender_profile', ]

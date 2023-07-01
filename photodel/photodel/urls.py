from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.api.urls', namespace='accounts')),
    path('api/additional_entities/', include('additional_entities.api.urls',
         namespace='additional_entities')),
    path('api/film_places/', include('film_places.api.urls', namespace='film_places')),
    path('api/gallery/', include('gallery.api.urls', namespace='gallery')),
    path('api/chat/', include('chat.api.urls', namespace='chat')),
    path('api/trainings/', include('trainings.api.urls', namespace='trainings')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

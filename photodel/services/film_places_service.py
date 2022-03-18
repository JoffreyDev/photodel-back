from django.db.models import Count, Case, When
from film_places.models import FilmPlaces, FilmPlacesLike


def get_popular_places():
    list_best_places = [place_id.get('place') for place_id in FilmPlacesLike.objects.values('place')
        .annotate(dcount=Count('place')).order_by('-dcount').values('place')]
    places = list(FilmPlaces.objects.filter(id__in=list_best_places) \
                 .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_best_places)], ))[:10])
    if len(places) < 10:
        places += list(FilmPlaces.objects.exclude(id__in=list_best_places))
    return places

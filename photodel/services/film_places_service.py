from django.db.models import Count, Case, When
from film_places.models import FilmPlaces, FilmPlacesLike


def get_popular_places(category):
    list_best_places = [place_id.get('place') for place_id in FilmPlacesLike.objects.values('place')
        .annotate(dcount=Count('place')).order_by('-dcount').values('place')]
    if category:
        places = list(FilmPlaces.objects.filter(id__in=list_best_places, category__name_category=category) \
                     .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_best_places)], ))[:10])
        return places
    else:
        places = list(FilmPlaces.objects.filter(id__in=list_best_places) \
                     .order_by(Case(*[When(id=n, then=i) for i, n in enumerate(list_best_places)], ))[:10])
    if len(places) < 10:
        places += list(FilmPlaces.objects.exclude(id__in=list_best_places))
    return places

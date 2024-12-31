from django.http import JsonResponse
from .models import PokeBerry
from django.db.models import Avg, Min, Max, Variance
from collections import Counter


def allBerryStats(request):
    
    # TODO: this might not be the best place for this logic
    # View should not implement logic at all
    # also, this values could be cached since the do not chage frequently
    aggregate = PokeBerry.objects.all().aggregate(
        min_growth_time=Min("growth_time"),
        max_growth_time=Max("growth_time"),
        variance_growth_time=Variance("growth_time"),
        avg_growth_time=Avg("growth_time"),
    )
    aggregate["frequency_growth_time"] = Counter(
        PokeBerry.objects.values_list("growth_time", flat=True)
    )
    aggregate["berries_names"] = ",".join(
        PokeBerry.objects.values_list("name", flat=True)
    )
    
    return JsonResponse(aggregate)

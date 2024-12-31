from django.http import JsonResponse
from .models import PokeBerry
from django.db.models import Avg, Min, Max, Variance
from collections import Counter
import matplotlib.pyplot as plt
from io import StringIO
from django.shortcuts import render


def get_pokeBerry_name_list():
    return ",".join(PokeBerry.objects.values_list("name", flat=True))


def calc_growth_time_frequencies():
    return Counter(PokeBerry.objects.values_list("growth_time", flat=True))


def calc_pokeBerry_stats():
    return PokeBerry.objects.all().aggregate(
        min_growth_time=Min("growth_time"),
        max_growth_time=Max("growth_time"),
        variance_growth_time=Variance("growth_time"),
        avg_growth_time=Avg("growth_time"),
    )


def build_histogram(lst):
    plt.hist(lst)

    imgdata = StringIO()
    plt.savefig(imgdata, format="svg")
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def allBerryStats(request):
    # TODO: this might not be the best place for this logic
    # View should not implement logic at all
    # also, this values could be cached since the do not chage frequently
    aggregate = calc_pokeBerry_stats()
    aggregate["frequency_growth_time"] = calc_growth_time_frequencies()
    aggregate["berries_names"] = get_pokeBerry_name_list()

    return JsonResponse(aggregate)


def pokeBerryGrowthTimeHistogram(request):
    graph = build_histogram(PokeBerry.objects.values_list("growth_time", flat=True))
    return render(request, 'histogram.html', {"graph":graph})

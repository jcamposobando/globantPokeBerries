from django.http import JsonResponse
import matplotlib.pyplot as plt
from io import StringIO
from django.shortcuts import render
from . import services

def build_histogram(lst):
    plt.hist(lst)

    imgdata = StringIO()
    plt.savefig(imgdata, format="svg")

    return imgdata.getvalue()


def allBerryStats(request):
    aggregate = services.calc_pokeBerry_stats()
    aggregate["frequency_growth_time"] = services.calc_growth_time_frequencies()
    aggregate["berries_names"] = services.get_pokeBerry_name_list()
    return JsonResponse(aggregate)


def pokeBerryGrowthTimeHistogram(request):
    graph = build_histogram(services.get_growth_time_list())
    return render(request, "histogram.html", {"graph": graph})


from django.http import JsonResponse, HttpResponse, HttpRequest
import matplotlib.pyplot as plt
from io import StringIO
from django.shortcuts import render
from . import services


def build_histogram(lst: list[int]) -> str:
    """Takes a list of integers and returns a string containing a histogram in svg formant

    Args:
        lst (list[int]): list of integers to build histogram

    Returns:
        str: A string containing a SVG-formatted histogram
    """
    image_data = StringIO()

    plt.hist(lst)
    plt.savefig(image_data, format="svg")

    return image_data.getvalue()


def allBerryStats(request: HttpRequest) -> JsonResponse:
    """Returns a JSON containing all pokeBerry Stats

    Args:
        request (HttpRequest): No parameter is read from the request at this time

    Returns:
        JsonResponse: JSON string containing all pokeBerry Stats
    """
    aggregate = services.calc_pokeBerry_stats()
    aggregate["frequency_growth_time"] = services.calc_growth_time_frequencies()
    aggregate["berries_names"] = ",".join(services.get_pokeBerry_name_list())
    return JsonResponse(aggregate)


def pokeBerryGrowthTimeHistogram(request: HttpRequest) -> HttpResponse:
    """Returns an HTML document containing a graph in SVG format

    Args:
        request (HttpRequest): No parameter is read from the request at this time

    Returns:
        HttpResponse: an HTML document containing a graph in SVG format
    """
    graph = build_histogram(services.get_growth_time_list())
    return render(request, "histogram.html", {"graph": graph})

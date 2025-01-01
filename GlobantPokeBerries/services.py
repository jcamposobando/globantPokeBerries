from .models import PokeBerry
from collections import Counter
from dataclasses import dataclass
from django.db.models import Avg, Min, Max, Variance
from statistics import median
import os
import requests


BASE_URL = "https://pokeapi.co/api/v2/berry"

@dataclass
class PokeBerryInfo():
    id: int
    name: str
    growth_time: int


def get_growth_time_list() -> list[int]:
    """Returns a list containing the growth_time of every pokeBerry

    Returns:
        list[int]: list containing the growth_time of every pokeBerry
    """
    return list(PokeBerry.objects.values_list("growth_time", flat=True))


def get_pokeBerry_name_list() -> list[str]:
    """Returns a list containing the name of every pokeBerry

    Returns:
        list[str]: list containing the name of every pokeBerry
    """
    return list(PokeBerry.objects.values_list("name", flat=True))


def calc_growth_time_frequencies() -> dict[int, int]:
    """Returns a dictionary in which the keys represent growth_time of pokeBerries and
    the value represents the amount of pokeBerries with said growth_time

    Returns:
        dict[int, int]: The key represents growth_time, the value represents its frequency
    """
    return Counter(get_growth_time_list())

def calc_growth_time_median() -> float:
    """Returns median value of pokeBerries growth_time

    Returns:
        float: Median value of pokeBerry growth_time
    """
    return median(get_growth_time_list())


def calc_pokeBerry_stats() -> dict[str, any]:
    """Runs the Min, Max, Variance and average aggregations of
    all the pokeBerries growth_time attribute

    Returns:
        dict[str, any]: returns a dictionary containing the aggregation of
        pokeBerries growth_time attribute
    """
    return PokeBerry.objects.all().aggregate(
        min_growth_time=Min("growth_time"),
        mean_growth_time=Avg("growth_time"),
        max_growth_time=Max("growth_time"),
        variance_growth_time=Variance("growth_time"),
    )


def get_number_of_berries():
    """Gets the number of berries on pokeapi
    Useful for iterating over berries

    Returns:
        int: count of pokeBerries
    """
    r = requests.get(f"{BASE_URL}")
    berry_response = r.json()
    return berry_response["count"]


def get_berry_info(id)->PokeBerryInfo:
    """Retrieves pokeBerry info by Id

    Args:
        id (int): Unique Id of each pokeBerry

    Returns:
        _type_: _description_
    """
    r = requests.get(f"{BASE_URL}/{str(id)}")
    berry = r.json()
    return PokeBerryInfo(**berry)


def load_all_berries_info():
    """Loads all berries info from pokeAPI into our database through the orm"""
    for i in range(1, get_number_of_berries() + 1):
        pokeBerry = PokeBerry(**get_berry_info(i))
        pokeBerry.save()


# It will run only once when module is loaded
# Avoid running it on dev, as it would run on every change
# because of hot-reloading
if os.getenv("DEBUG_VALUE") != "TRUE":
    load_all_berries_info()

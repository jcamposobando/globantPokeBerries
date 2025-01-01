import requests
from django.db.models import Avg, Min, Max, Variance
from collections import Counter
from .models import PokeBerry
import os

BASE_URL = "https://pokeapi.co/api/v2/berry"


def get_growth_time_list():
    return PokeBerry.objects.values_list("growth_time", flat=True)


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


def get_number_of_berries():
    """Gets the number of berries on pokeapi
    Useful for iterating over berries

    Returns:
        int: count of pokeBerries
    """
    r = requests.get(f"{BASE_URL}")
    berry_response = r.json()
    return berry_response["count"]


def get_berry_info(id):
    """Retrieves pokeBerry info by Id

    Args:
        id (int): Unique Id of each pokeBerry

    Returns:
        _type_: _description_
    """
    r = requests.get(f"{BASE_URL}/{str(id)}")
    berry = r.json()
    return {
        "id": berry["id"],
        "name": berry["name"],
        "growth_time": berry["growth_time"],
    }


def load_berry_info():
    number_of_berries = get_number_of_berries()
    for i in range(1, number_of_berries + 1):
        pokeBerry = PokeBerry(get_berry_info(i))
        pokeBerry.save()


# It will run only once
# Avoid running it on dev, as it would run on every change
if os.getenv("DEBUG_VALUE") != "TRUE":
    load_berry_info()

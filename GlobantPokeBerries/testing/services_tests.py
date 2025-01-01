from GlobantPokeBerries import services
from GlobantPokeBerries.models import PokeBerry
from statistics import StatisticsError
import pytest
import requests
import requests_mock
import json
from dataclasses import asdict


# calc_growth_time_frequencies
class Test_calc_growth_time_frequencies:

    @pytest.mark.django_db
    def test_empty_list(self):
        assert len(services.calc_growth_time_frequencies()) == 0

    @pytest.mark.django_db
    def test_different_frequencies(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=2).save()
        assert services.calc_growth_time_frequencies() == {1: 1, 2: 1}

    @pytest.mark.django_db
    def test_same_frequencies(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=1).save()
        assert services.calc_growth_time_frequencies() == {1: 2}


# calc_growth_time_median
class Test_calc_growth_time_median:

    @pytest.mark.django_db
    def test_empty_list(self):
        with pytest.raises(StatisticsError):
            services.calc_growth_time_median()

    @pytest.mark.django_db
    def test_even_count(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=2).save()
        assert services.calc_growth_time_median() == 1.5

    @pytest.mark.django_db
    def test_odd_count(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=3).save()
        assert services.calc_growth_time_median() == 2


# calc_pokeBerry_stats
class Test_calc_pokeBerry_stats:

    @pytest.mark.django_db
    def test_empty_list(self):
        assert services.calc_pokeBerry_stats() == {
            "max_growth_time": None,
            "mean_growth_time": None,
            "min_growth_time": None,
            "variance_growth_time": None,
        }

    @pytest.mark.django_db
    def test_odd_count(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=3).save()
        assert services.calc_pokeBerry_stats() == {
            "max_growth_time": 3,
            "mean_growth_time": 2.0,
            "min_growth_time": 1,
            "variance_growth_time": 1.0,
        }


# get_berry_info
class Test_get_berry_info:
    def test_get_berry_info_empty(self, requests_mock):
        with pytest.raises(TypeError):
            requests_mock.get(services.BASE_URL + "/1", text="")
            services.get_berry_info()

    def test_get_berry_info_valid(self, requests_mock):
        remote_pokeberry = {"id": 1, "name": "a", "growth_time": 1}
        requests_mock.get(services.BASE_URL + "/1", text=json.dumps(remote_pokeberry))
        pokeBerry = services.get_berry_info(1)
        assert asdict(pokeBerry) == remote_pokeberry


# get_growth_time_list
class Test_get_growth_time_list:

    @pytest.mark.django_db
    def test_empty_list(self):
        assert services.get_growth_time_list() == []

    @pytest.mark.django_db
    def test_odd_count(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=2).save()
        PokeBerry(id=3, name="c", growth_time=3).save()
        assert services.get_growth_time_list() == [1, 2, 3]


# get_number_of_berries
class Test_get_number_of_berries:
    def test_get_number_of_berries_empty(self, requests_mock):
        with pytest.raises(KeyError):
            requests_mock.get(services.BASE_URL, text="{ }")
            services.get_number_of_berries()

    def test_get_number_of_berries_valid(self, requests_mock):
        requests_mock.get(services.BASE_URL, text='{"count":1}')
        pokeBerryCount = services.get_number_of_berries()
        assert pokeBerryCount == 1


# get_pokeBerry_name_list
class Test_get_pokeBerry_name_list:

    @pytest.mark.django_db
    def test_empty_list(self):
        assert services.get_pokeBerry_name_list() == []

    @pytest.mark.django_db
    def test_odd_count(self):
        PokeBerry(id=1, name="a", growth_time=1).save()
        PokeBerry(id=2, name="b", growth_time=2).save()
        PokeBerry(id=3, name="c", growth_time=3).save()
        assert services.get_pokeBerry_name_list() == ["a", "b", "c"]

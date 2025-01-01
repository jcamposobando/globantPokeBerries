from GlobantPokeBerries import services
from GlobantPokeBerries.models import PokeBerry
from statistics import StatisticsError
import pytest


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
        assert services.get_pokeBerry_name_list() == ["a","b","c"]

# load_all_berries_info

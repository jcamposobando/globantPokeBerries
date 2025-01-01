import pytest
from GlobantPokeBerries.models import PokeBerry
from django.db.utils import IntegrityError

# We did not implement much functionality at the Model level, so this tests are brief


@pytest.mark.django_db
def test_make_poke_berry():
    test_id = 1000
    test_name = "test"
    pokeBerry = PokeBerry(id=test_id, name=test_name, growth_time=1)
    pokeBerry.save()
    assert PokeBerry.objects.get(pk=test_id).name == test_name


@pytest.mark.django_db
def test_exception_when_id_missing():
    with pytest.raises(IntegrityError):
        test_name = "test"
        pokeBerry = PokeBerry(name=test_name)
        pokeBerry.save()


@pytest.mark.django_db
def test_pokeberry_string():
    test_id = 1000
    test_name = "test"
    pokeBerry = PokeBerry(id=test_id, name=test_name, growth_time=1)
    pokeBerry.save()
    assert str(PokeBerry.objects.get(pk=test_id)) == "1000-test"

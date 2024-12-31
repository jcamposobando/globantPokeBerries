import requests

BASE_URL = "https://pokeapi.co/api/v2/berry"

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
        "id":berry["id"],
        "name":berry["name"],
        "growth_time":berry["growth_time"]}
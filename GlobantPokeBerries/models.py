from django.db import models
from . import services
import os

class PokeBerry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    growth_time = models.IntegerField()

    # Implementing this methods gives us a nicer string representation
    # Kindly refer to https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api
    def __str__(self):
        return f"{self.id}-{self.name}"


# This might not be the best place for this logic, as it does not belong to the model itself
# By placing it here it runs only once, when the server starts running
def load_berry_info ():
    number_of_berries = services.get_number_of_berries()
    print(f"number of berries:{number_of_berries}")
    for i in range(1, number_of_berries + 1):
        # Cool destructurin assigment, buy maybe brittle, check later
        pokeBerry = PokeBerry(**services.get_berry_info(i))
        print(pokeBerry)
        pokeBerry.save()

#Avoid running it on dev, as it would run on every change
if (os.getenv("DEBUG_VALUE")!="TRUE"):
    load_berry_info()

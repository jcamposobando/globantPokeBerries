from django.db import models


class PokeBerry(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    growth_time = models.IntegerField()

    # Implementing this methods gives us a nicer string representation
    # Kindly refer to https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api
    def __str__(self):
        return f"{self.id}-{self.name}"

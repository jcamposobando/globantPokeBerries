# This file contains settings for the admin interface
# It was added to be able to edit pokeBerries from the admin url
# Please refer to https://docs.djangoproject.com/en/5.1/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin

from django.contrib import admin

from .models import PokeBerry

admin.site.register(PokeBerry)
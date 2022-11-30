from django.contrib import admin
from imdb.models import Imdb


@admin.register(Imdb)
class ImdbAdmin(admin.ModelAdmin):
    list_display = ['imdb_id', 'title', 'rate', 'director', 'country_of_origin', 'language', 'run_time']

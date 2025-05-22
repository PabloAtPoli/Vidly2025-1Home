from django.contrib import admin

from .models import Genre, Movie

admin.site.site_header = "Vidly Administration" # This is the title of the admin page
admin.site.site_title = "Vidly Admin Panel" # This is the title of the browser tab
admin.site.index_title = "Data Overview" # This is the title of the home page

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields= ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')
    list_filter = ('genre', 'release_year', 'date_created')
    exclude = ('date_created',)
    search_fields = ('title', 'release_year', 'genre__name')  # Fields to search

# Regisr your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from . models import Genre, Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = get_object_or_404(Movie,id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})




from django.shortcuts import render, redirect
from genre.models import Genre
from games.models import Game
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    request.session['ver'] = False
    genres1 = Genre.objects.order_by('name')[:3]
    genres2 = Genre.objects.order_by('name')[3:6]
    genres = zip(genres1, genres2)
    recent = Game.objects.order_by('-created')[:2]
    context = {'genres': genres, 'recent':recent}
    return render(request, "home.html", context)


@login_required
def genreView(request, genre_slug):
    genre = Genre.objects.get(genre_slug = genre_slug)
    games = Game.objects.filter(genre = genre)
    p = Paginator(games, 12)
    context = {'genre':genre, 'qs': games, 'page_obj': p}
    

    return render(request, "genre.html", context)

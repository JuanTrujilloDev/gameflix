from django.db.models import Q
from django.shortcuts import render, redirect
from genre.models import Genre
from games.models import Game
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request):

    request.session['ver'] = False
    genres1 = Genre.objects.order_by('name')[:3]
    genres2 = Genre.objects.order_by('name')[3:6]
    genres = zip(genres1, genres2)
    recent = Game.objects.order_by('-created')[:3]
    context = {'genres': genres, 'recent':recent}
    return render(request, "home.html", context)

#GenreView
@login_required
def genreView(request, genre_slug):
    genre = Genre.objects.get(genre_slug = genre_slug)
    games = Game.objects.filter(genre = genre)
    games = games.order_by('-pk')
    p = Paginator(games, 12)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'genre':genre, 'qs': games, 'page_obj': page_obj}
    

    return render(request, "genre.html", context)

#Search view, query.
class SearchView(LoginRequiredMixin ,ListView):
    model = Game
    template_name = "search.html"
    context_object_name = "games"
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        games = Game.objects.filter(
            Q(name__icontains=query) | Q(cracker__icontains=query) | Q(genre__name__icontains=query)
        )
        return games
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')

        return context


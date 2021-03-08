from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Game
from genre.models import Genre
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class GameView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] =  Genre.objects.all()
        return context

class GameDetail(LoginRequiredMixin, DetailView):
    model = Game
    template_name = 'gamedetail.html'
    
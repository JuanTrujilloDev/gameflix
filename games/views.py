from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseForbidden
from django.urls import reverse
from .models import Game
from genre.models import Genre
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormMixin
from comments.forms import NewComment

# Create your views here.

class GameView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'games.html'
    ordering = ['-pk']
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] =  Genre.objects.all()
        return context

class GameDetail(FormMixin ,LoginRequiredMixin,  DetailView):
    model = Game
    template_name = 'gamedetail.html'
    form_class = NewComment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['comments'] = Comment.objects.filter(game = self.object)
        context['comments'] = context['comments'].order_by('-date')
        
        return context

    def get_success_url(self):
        return reverse('game-detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        obj = form.save(commit = False)
        obj.author = self.request.user
        self.object = self.get_object()
        obj.game = self.object
        obj.save()
        return super().form_valid(form)



    
    
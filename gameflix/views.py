from django.shortcuts import render, redirect
from genre.models import Genre

# Create your views here.

def home(request):

    request.session['ver'] = False
    genres1 = Genre.objects.order_by('name')[:3]
    genres2 = Genre.objects.order_by('name')[3:6]
    genres = zip(genres1, genres2)
    context = {'genres': genres}
    return render(request, "home.html", context)

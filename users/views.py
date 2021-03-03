from django.shortcuts import render, redirect
from .forms import UserRegisterForm, AuthenticationForm, UserUpdateForm

from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from random import randint

from django.urls import reverse
from django.views.generic import UpdateView, DeleteView

from django.contrib import messages


# Create your views here.


def register(request):

    if request.user.is_authenticated:
        return redirect('home-view')
    
    form = UserRegisterForm()
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'Your account has been created!')
            return redirect('home-view')
    else:
        messages.warning(request,  'There was an issue creating your account.')
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

@login_required
def verificationView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            request.session['ver'] = True
            messages.success(request,  'You can now edit your account.')
            return redirect('settings-view')

        else:
            request.session['ver'] = False
            messages.danger(request,  'Wrong authentication!')
            return render(request, 'authenticate.html', {'form': form})

    else:
        request.session['ver'] = False
        return render(request, 'authenticate.html', {'form': form})





@login_required
def settingsView(request):
    if request.session['ver']:
        form = UserUpdateForm(instance = request.user)
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance= request.user)
            if form.is_valid():
                messages.success(request, 'You account has been updated!')
                form.save()
                request.session['ver'] = False
                return redirect('home-view')

            else:
                messages.warning(request,  'There was an issue updating your account.')
                return render(request, 'settings.html', {'form': form})

        else:
            return render(request, 'settings.html', {'form': form})

    else:
        return redirect('verification-view')



def userDeleteView(request):

    if request.session['ver']:
        if request.method == 'POST':
            obj = request.user
            obj.delete()
            return redirect('home-view')

        else:
            messages.warning(request,  "Don't leave yet!.")
            return render(request, 'user_confirm_delete.html')

     

    else:
        return redirect('verification-view')



   


        
    
    







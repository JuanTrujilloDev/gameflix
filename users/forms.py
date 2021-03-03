from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        


    def clean_password(self):

        password = self.cleaned_data['password1']
        password_confirm = self.cleaned_data['password2']

        if password != password_confirm:
            raise forms.ValidationError(
        "Password don't match!")

        else:
            return (password, password_confirm)


    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email__iexact=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email


    def clean_username(self):

        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username__iexact=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username


class AuthenticationForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)


    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data['username']
        user = User.objects.get(username__iexact = username)

        if user.check_password(password):
            return password

        else: 
            raise forms.ValidationError('Password is invalid!')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):

        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email__iexact=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email


    def clean_username(self):

        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username__iexact=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username
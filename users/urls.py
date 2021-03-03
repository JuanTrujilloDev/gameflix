from django.urls import path
from django.contrib.auth.views import  (LogoutView, LoginView, PasswordResetView 
                                    , PasswordResetDoneView,
                                    PasswordResetConfirmView,
                                    PasswordResetCompleteView)
from .views import (
    register,
    verificationView,
    settingsView,
    userDeleteView,
)

urlpatterns = [
    path('register/', register, name="register-view"),
    path('login/', LoginView.as_view(template_name="login.html"), name = "login-view"),
    path('logout/', LogoutView.as_view(), name="logout-view"),
    path('verification/', verificationView, name="verification-view"),
    path('settings/', settingsView, name="settings-view"),
    path('delete/', userDeleteView, name="delete-view"),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/done/',
         PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
             name="password_reset_complete"
         ), 
]

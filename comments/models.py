from django.db import models
from django.contrib.auth.models import User
from games.models import Game

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField(max_length = 280)
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now= True)

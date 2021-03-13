from django.db import models
from genre.models import Genre
from django.utils.text import slugify
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=25)

    image = models.ImageField(upload_to="games", default = 'games/default.jpg',
    validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png']) ])
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    cracker = models.CharField(max_length=35)
    desc = models.TextField(max_length = 150)
    requirements = models.TextField()
    created = models.DateField(auto_now = False)
    slug = models.SlugField(blank = True, null=True)
    download = models.CharField(max_length= 100)
    size = models.CharField(max_length=10)
    lang = models.CharField(max_length=10)
    trailer = EmbedVideoField(default=" ")


    def save(self, *args, **kwargs):
        super(Game, self).save()
        pk = str(self.pk)
        self.slug = slugify(self.name) + pk
        super(Game, self).save(*args, **kwargs)
        
      

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game-detail", kwargs={"slug": self.slug})
    


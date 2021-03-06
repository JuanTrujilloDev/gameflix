from django.db import models
from genre.models import Genre
from django.utils.text import slugify
from PIL import Image

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to="games")
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    cracker = models.CharField(max_length=30)
    desc = models.TextField()
    created = models.DateField(auto_now = False)
    game_slug = models.SlugField(blank = True, null=True)

    def save(self, *args, **kwargs):
        self.game_slug = slugify(self.name)
        super().save()
        img = Image.open(self.image.path)

        if img.height > 280 or img.width > 380:
            output_size = (280 , 380)
            img.thumbnail(output_size)
            img.save(self.image.path) 

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


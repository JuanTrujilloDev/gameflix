from django.db import models
from PIL import Image
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(blank=False, null= False, max_length=20)
    image = models.ImageField(upload_to='genre', default= 'genre\default_genre.jpg',
    validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png']) ] ) 
    desc = models.TextField(blank= False, null = False, max_length = 50)
    genre_slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.genre_slug = slugify(self.name)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 650 or img.width > 600:
            output_size = (650 , 550)
            img.thumbnail(output_size)
            img.save(self.image.path) 

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'genre/{self.genre_slug}'
    

        



   
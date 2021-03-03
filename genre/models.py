from django.db import models
from PIL import Image
from django.utils.text import slugify

# Create your models here.
class Genre(models.Model):
    name = models.CharField(blank=False, null= False, max_length=20)
    image = models.ImageField(upload_to='genre', default= 'genre\default_genre.jpg')
    desc = models.TextField(blank= False, null = False, max_length = 50)
    slug = models.SlugField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 650 or img.width > 600:
            output_size = (650 , 550)
            img.thumbnail(output_size)
            img.save(self.image.path) 

        



   
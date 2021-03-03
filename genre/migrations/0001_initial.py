# Generated by Django 3.1.5 on 2021-03-03 18:48

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='default_genre.jpg', force_format=None, keep_meta=True, null=True, quality=0, size=[630, 565], upload_to='genre')),
                ('desc', models.TextField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
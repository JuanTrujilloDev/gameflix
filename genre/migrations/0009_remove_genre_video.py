# Generated by Django 3.1.7 on 2021-03-07 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0008_auto_20210307_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='video',
        ),
    ]

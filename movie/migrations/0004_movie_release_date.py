# Generated by Django 4.1.7 on 2023-03-20 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 20, 11, 56, 18, 544113)),
        ),
    ]

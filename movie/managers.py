from django.db import models



class GenreManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genre='action')
    def longest_movies(self):
        return super().get_queryset().filter(duration_mins__gte='3.50')
    def shortest_movies(self):
        return super().get_queryset().filter(duration_mins__gte='2')

class ScifiManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genre='sci-fic')
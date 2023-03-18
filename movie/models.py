from django.db import models


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    genre =models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.title
    class meta:
         db_table="movie"




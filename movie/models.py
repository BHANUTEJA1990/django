from django.db import models
from datetime import datetime
from .managers import GenreManager, ScifiManager

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    genre =models.CharField(max_length=15,null=True)
    release_date=models.DateTimeField(default=datetime.now())
    duration_mins=models.IntegerField(default=0)
    #email=models.EmailField(max_length=30)
    mvmgr=models.Manager()
    objects=models.Manager()
    Action_mgr=GenreManager()
    scifi_mgr=ScifiManager()

    def __str__(self):
       # return self.title
        return self.title + ", " + self.director + self.genre + str(self.release_date) + str(self.duration_mins)
    class Meta:
        db_table="movie"
        ordering=['title','director']
        #get_latest_by=['release_date']
        get_latest_by=['-release_date']





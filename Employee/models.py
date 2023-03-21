from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Employee(models.Model):
    fname=models.CharField(max_length=20)
    iname=models.CharField(max_length=20)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.fname
    class meta:
         db_table="employee"
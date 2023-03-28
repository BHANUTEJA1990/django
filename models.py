from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)

    class Meta:
        db_table='person'

class Citizenship(models.Model):
    person=models.OneToOneField(Person,on_delete=models.CASCADE)
    country=models.CharField(max_length=20)

    class Meta:
        db_table="Citizenship"




class Department(models.Model):
    name=models.CharField(max_length=20)
    class Meta:
        db_table="department"

class Workers(models.Model):
    fn=models.CharField(max_length=20)
    ln=models.CharField(max_length=20,null=True)
    dep=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name="empdep")
    def __str__(self):
        return str(self.fn)+""+str(self.ln)
    class Meta:
        db_table="Workers"

class Bank(models.Model):
    name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20,null=True)

    class Meta:
        db_table="bank"
class Customer(models.Model):
    fn=models.CharField(max_length=20)
    ln=models.CharField(max_length=20,null=True)
    bank=models.ManyToManyField(Bank,null=True,related_name="customerb")
    class Meta:
        db_table="customer"

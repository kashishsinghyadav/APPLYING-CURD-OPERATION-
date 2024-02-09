from django.db import models

class Position(models.Model):
    title=models.CharField(max_length=50)

class Emp(models.Model):
    firstname=models.CharField(max_length=13)
    mobile=models.CharField(max_length=15)
    empcode=models.CharField(max_length=3)
    pos=models.ForeignKey(Position,on_delete=models.CASCADE)


# Create your models here.

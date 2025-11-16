from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=29)
    lastname=models.CharField(max_length=39)
    testscore=models.FloatField() 

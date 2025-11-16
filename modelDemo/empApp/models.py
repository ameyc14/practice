from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=39)
    lastname=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=45)
class Programmer(models.Model):
    name=models.CharField(max_length=20)
    sal=models.IntegerField()
class Project(models.Model):
    name=models.CharField(max_length=30)
    programmers=models.ManyToManyField(Programmer)

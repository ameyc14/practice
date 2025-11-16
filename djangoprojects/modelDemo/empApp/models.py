from django.db import models


class Employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    salary=models.FloatField()
    email=models.CharField(max_length=40)

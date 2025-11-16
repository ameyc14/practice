from django.db import models

# Create your models here.
class studentinfo(models.Model):
    name=models.CharField(max_length=30)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()

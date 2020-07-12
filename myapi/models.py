from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    Glucose = models.IntegerField()
    insulin = models.IntegerField()
    BMI = models.FloatField()
    Diabetesfunction = models.FloatField()
    Age = models.IntegerField()
    result = models.BooleanField()

    def __str__(self):
        return self.name

from django.db import models

class Calculation(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField()
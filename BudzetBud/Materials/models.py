from django.db import models



class Material(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    type = models.Charfield()

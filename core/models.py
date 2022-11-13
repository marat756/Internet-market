from django.db import models

class Jacet(models.Model):
    nomi = models.CharField(max_lenght=20)
    rangi = models.CharField(max_lenght=20)




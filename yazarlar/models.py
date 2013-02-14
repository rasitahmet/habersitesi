from django.db import models


class Yazar(models.Model):
    yazaradi = models.CharField(max_length=200)
    unvan = models.CharField(max_length=100)
    brans = models.CharField(max_length=100)

class Yazi(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.CharField(max_length=500)
    yazi = models.TextField()
    tarih = models.DateTimeField('eklendigi tarih')
    yazar = models.ForeignKey('Yazar', related_name='yazilar')
# Create your models here.

from django.db import models

class Roportaj(models.Model):
    baslik = models.CharField(max_length=300)
    konuk = models.CharField(max_length=300)
    aciklama = models.CharField(max_length=500)
    icerik = models.TextField()
    tarih = models.DateTimeField('eklendigi tarih')

# Create your models here.

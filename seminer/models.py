from django.db import models


class Seminer(models.Model):
    baslik = models.CharField(max_length=300)
    resim = models.ImageField(upload_to='resim/%Y/%m/%d')
    aciklama = models.CharField(max_length=600)
    tarih = models.DateTimeField('eklendigi tarih')

# Create your models here.

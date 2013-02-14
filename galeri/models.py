from django.db import models

class Album(models.Model):
    baslik = models.CharField(max_length=300)
    aciklama = models.CharField(max_length=500)
    kapak = models.ImageField(upload_to='galeri/%Y/%m/%d')
    tarih = models.DateTimeField('eklendigi tarih')

def __unicode__(self):
        return self.baslik

class Resim(models.Model):
    album = models.ForeignKey('Album', related_name='resimler')
    resim = models.ImageField(upload_to='galeri/%Y/%m/%d')
    aciklama = models.CharField(max_length=500)
    tarih = models.DateTimeField('eklendigi tarih')

def __unicode__(self):
        return self.aciklama
# Create your models here.

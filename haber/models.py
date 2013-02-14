from django.db import models

class Haber(models.Model):
    baslik = models.CharField(max_length=300)
    aciklama = models.CharField(max_length=500)
    icerik = models.TextField()
    kapak = models.ImageField(upload_to='haber/kapak_resim', blank=False)
    tarih = models.DateTimeField("yayinlanma tarihi")

def __unicode__(self):
        return self.baslik

class HaberResim(models.Model):
    haber = models.ForeignKey('Haber', related_name='resimler')
    resim = models.ImageField(upload_to='resim/%Y/%m/%d', blank=False)
    aciklama = models.CharField(max_length=300, blank=True)
    
def __unicode__(self):
        return self.resim

# Create your models here.

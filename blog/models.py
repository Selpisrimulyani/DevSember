from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=40)
    keterangan = models.TextField()

    def __unicode__(self):
      return self.nama



class Berita(models.Model):
 judul = models.CharField(max_length=50)
 tanggal = models.DateField()
 kategori = models.ForeignKey(Kategori, default=False)
 konten = models.TextField()
 publish = models.BooleanField(default=True)

 def __unicode__(self):
   return self.judul

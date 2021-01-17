from django.db import models
from django.urls import reverse

class Tur(models.Model):
    adi = models.CharField(max_length=200,help_text="Bir kitap türü giriniz (Duygusal Romantik gibi)")

    def __str__(self):
        return self.adi


class Kitap(models.Model):
    baslik = models.CharField(max_length=200)
    yazar = models.ForeignKey('Yazar',on_delete=models.SET_NULL,null=True)
    ozet = models.TextField(max_length=1000)
    isbn = models.CharField('ISBN',max_length=13)
    tur = models.ManyToManyField(Tur)

    def __str__(self):
        return self.baslik


import uuid

class KitapGiris(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4)
    kitap = models.ForeignKey('Kitap',on_delete=models.SET_NULL,null=True)
    imyazi = models.CharField(max_length=200)
    geri_donus = models.DateField(null=True,blank=True)

    KITAP_DURUM = (
        ('G','Rafta'),
        ('U','Ulaşılabilir'),
        ('K','Kirada'),
        ('R','Rezerve'),
    )

    durum = models.CharField(max_length=1,choices=KITAP_DURUM,blank=True,default='G')

    class Meta:
        ordering = ['geri_donus']

    def __str__(self):
        return f'{self.id} ({self.kitap.baslik})'


class Yazar(models.Model):
    adi = models.CharField(max_length=100)
    soyadi = models.CharField(max_length=100)
    dogum_tarihi = models.DateField(null=True,blank=True)
    olum_tarihi = models.DateField('Öldü',null=True,blank=True)

    class Meta:
        ordering = ['soyadi','adi']

    def __str__(self):
        return f'{self.soyadi},{self.adi}'
    
from django.db import models
from django.utils import timezone

class Sorular(models.Model):
    soru_cumlesi = models.CharField(max_length=200)
    kayit_zaman = models.DateTimeField(default=timezone.now)
    yayim_zaman = models.DateTimeField('yayim_zamani')

    def __str__(self):
        return str(self.id) + "_" + self.soru_cumlesi[:9]

class Secenek(models.Model):
    soru = models.ForeignKey(Sorular,on_delete=models.CASCADE)
    secenek_metin = models.CharField(max_length=200)
    cevap = models.IntegerField(default=0)

    def __str__(self):
        return str(self.soru.id) + "_" + str(self.id)


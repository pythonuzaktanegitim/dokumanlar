from django.db import models
from django.utils import timezone
import datetime

class Sorular(models.Model):
    soru_cumlesi = models.CharField(max_length=200)
    yayim_zaman = models.DateTimeField()

    def __str__(self):
        return self.soru_cumlesi
    
    def son_zaman_sorular(self):
        simdi = timezone.now()
        return  simdi - datetime.timedelta(days=1) <= self.yayim_zaman <= simdi
        

class Secenek(models.Model):
    soru = models.ForeignKey(Sorular,on_delete=models.CASCADE)
    sec_metin = models.CharField(max_length=200)
    cevap = models.IntegerField(default=0)

    def __str__(self):
        return self.sec_metin
    
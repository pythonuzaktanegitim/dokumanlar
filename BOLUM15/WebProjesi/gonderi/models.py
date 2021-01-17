from django.db import models

class Gonderi(models.Model):
    baslik = models.TextField()
    resim = models.ImageField(upload_to='resimler/')

    def __str__(self):
        return self.baslik
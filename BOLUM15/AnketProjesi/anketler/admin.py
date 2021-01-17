from django.contrib import admin
from .models import Sorular

class SorularAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields':["soru_cumlesi"]}),
        ("Yıl Bilgisi" ,{'fields': ["yayim_zaman"]}),
    ]




admin.site.register(Sorular,SorularAdmin)

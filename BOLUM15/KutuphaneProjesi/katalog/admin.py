from django.contrib import admin
from .models import Yazar,KitapGiris,Kitap,Tur

class YazarAdmin(admin.ModelAdmin):
    list_display = ('soyadi','adi','dogum_tarihi','olum_tarihi')
    fields = ['adi','soyadi',('dogum_tarihi','olum_tarihi')]
admin.site.register(Yazar,YazarAdmin)

@admin.register(KitapGiris)
class KitapGirisAdmin(admin.ModelAdmin):
    list_filter = ('durum','geri_donus')
    fieldsets = (
        (None, {'fields':('kitap','imyazi','id')}),
        ('Ulaşılabilirlik',{'fields':('durum','geri_donus')})
    )

class KitapGirisInLine(admin.TabularInline):
    model = KitapGiris

@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display=('baslik','yazar')
    inlines = [KitapGirisInLine]



admin.site.register(Tur)
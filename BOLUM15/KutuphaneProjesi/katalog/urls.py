from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('kitaplar/',views.KitapListeView.as_view(),name='kitaplar'),
    path('kitap/<int:pk>/',views.kitapDetay,name="kitap_detay"),
    path('yazarlar/',views.yazarListe,name='yazarlar'),
    path('yazar/<int:pk>/',views.yazarDetay,name='yazar_detay'),
    path('yazar/yeni/',views.yeniYazar,name="yeni_yazar"),

]

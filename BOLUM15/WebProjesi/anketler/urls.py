from django.urls import path
from . import views

urlpatterns = [
    path('',views.liste,name="liste"),
    path('simdi/',views.simdi_zaman,name="simdi"),
    path('liste/',views.liste,name="liste"),
]

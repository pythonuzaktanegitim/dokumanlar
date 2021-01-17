from django.urls import path
from . import views

urlpatterns = [
    path('eposta/',views.emailView,name="email"),
    path('gonderildi/',views.gonderView,name="gonderildi")
]



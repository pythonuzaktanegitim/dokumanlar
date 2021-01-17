from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,Http404
import datetime
from .models import Sorular

def index(request):
    return HttpResponse("Merhaba Hoşgeldiniz")


def simdi_zaman(request):
    simdi = datetime.datetime.now()
    # html = "<html><body>Şimdi %s.</body></html>" % simdi
    raise Http404("Sayfa Bulunamadı")


def liste(request):
    sorular = Sorular.objects.all()
    return render(request,"Anketler/SoruListe.html",{"sorular":sorular})

    
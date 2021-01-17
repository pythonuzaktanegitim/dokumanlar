from django.shortcuts import render,get_object_or_404,redirect
from .models import Yazar,KitapGiris,Kitap,Tur
from django.views import generic
from .forms import YazarForm

def index(request):

    toplam_kitap = Kitap.objects.all().count()
    giris_sayisi = KitapGiris.objects.all().count()

    ulasilabilir_kitap = KitapGiris.objects.filter(durum__exact='U').count()

    yazar_sayisi = Yazar.objects.all().count()

    icerik = {
        'toplam_kitap':toplam_kitap,
        'giris_sayisi':giris_sayisi,
        'ulasilabilir_kitap':ulasilabilir_kitap,
        'yazar_sayisi':yazar_sayisi,
        
    }

    return render(request,'index.html',context=icerik)


class KitapListeView(generic.ListView):
    model=Kitap
    context_object_name = 'kitap_listesi'
    queryset = Kitap.objects.all()
    template_name = 'kitaplar/liste.html'

def kitapDetay(request,pk):
    k = get_object_or_404(Kitap,pk=pk)
    return render(request,"kitaplar/kitap_detay.html",{'kitap':k})

def yazarListe(request):
    yazarlar = Yazar.objects.all()
    return render(request,'yazarlar/yazar_liste.html',{'yazarlar':yazarlar})

def yazarDetay(request,pk):
    yaz = get_object_or_404(Yazar,pk=pk)
    return render(request,"yazarlar/yazar_detay.html",{'yazar':yaz})


def yeniYazar(request):
    if request.method == "POST":
        form = YazarForm(request.POST)
        if form.is_valid():
            yazar = form.save(commit=False)
            yazar.save()
            return redirect('yazar_detay',pk=yazar.pk)
    else:
        form = YazarForm()
    return render(request,'yazarlar/yazar_form.html',{'form':form})
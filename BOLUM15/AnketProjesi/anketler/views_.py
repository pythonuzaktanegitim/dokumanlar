from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Sorular
from django.template import loader
from django.urls import reverse

def index(request):
    son_zaman_sorular = Sorular.objects.order_by('-yayim_zaman')[:5]

    # template = loader.get_template('anketler/index.html')
    # icerik = {
    #     'son_zaman_sorular' : son_zaman_sorular
    # }
    # return HttpResponse(template.render(icerik,request))

    return render(request,'anketler/index.html',{'son_zaman_sorular':son_zaman_sorular})

def detay(request,soru_id):
    # try:
    #     soru = Sorular.objects.get(pk=soru_id)
    # except Sorular.DoesNotExist:
    #     raise Http404("Soru Bulunamadı")
    # return render(request,"anketler/detay.html",{'soru':soru})
    soru = get_object_or_404(Sorular,pk=soru_id)
    return render(request,"anketler/detay.html",{'soru':soru})

def sonuclar(request,soru_id):
    soru = get_object_or_404(Sorular,pk=soru_id)
    return render(request,"anketler/sonuclar.html",{"soru":soru})

def cevap(request,soru_id):
    soru =get_object_or_404(Sorular,pk=soru_id)
    try:
        secilen_cevap = soru.secenek_set.get(pk=request.POST["secenek"])
    except (KeyError,Secenek.DoesNotExists):
        return render(request,"anketler/detay.html",{
            'soru':soru,
            'hata_mesaji':'Cevaplamadınız'
        })
    else:
        secilen_cevap.cevap += 1
        secilen_cevap.save()

    return HttpResponseRedirect(reverse('anketler:sonuclar', args=(soru.id,)))

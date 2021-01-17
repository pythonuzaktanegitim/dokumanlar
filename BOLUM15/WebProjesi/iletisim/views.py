from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from .forms import IletisimForm


def emailView(request):
    if request.method == "GET":
        form = IletisimForm()
    else:
        form = IletisimForm(request.POST)
        if form.is_valid():
            konu = form.cleaned_data['konu']
            kimden = form.cleaned_data['kimden']
            mesaj = form.cleaned_data['mesaj']
            try:
                send_mail(konu,mesaj,kimden,["admin@ornek.com"])
            except BadHeaderError:
                return HttpResponse("Geçersiz Form")
            return redirect("gonderildi")
    return render(request,"Iletisim/eposta.html",{'form':form})


def gonderView(request):
    return HttpResponse("Mesajın için teşekkür ederiz")

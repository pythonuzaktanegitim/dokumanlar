from tkinter import *
from tkinter import  messagebox
pencere = Tk()
pencere.title("TK 14.3_2")
pencere.geometry("300x300+200+200")
def tikla():
    messagebox.showwarning("Bilgi Mesajı","Düğmeye Tıkladın")
def soruSor():
    cevap = ""
    elCevap = messagebox.askyesnocancel("Soru Soruma","Emin misin?")
    if elCevap:
        cevap = messagebox.askyesno("Soru Sorma","Baak Sana Diyorum?")
    print(cevap)
dugme = Button(pencere,text="Tıkla",command=tikla)
dugme.grid(column=0,row=0)
dugme2 = Button(pencere,text="Soru Sorma",command=soruSor)
dugme2.grid(column=0,row=2)
##################################################
def aktarim():
    etiket["text"] = str(veri.get()) + "-" + str(bar["value"])

veri = IntVar()
veri.set(36)
spin = Spinbox(pencere,from_=0,to=100,width=10,textvariable=veri)
spin.grid(column=0,row=3)

from tkinter.ttk import  Progressbar
bar = Progressbar(pencere,length=100)
bar["value"] = 70
bar.grid(column=1,row=3)
dugme3 = Button(pencere,text="Spin Aktar",command=aktarim)
dugme3.grid(column=2,row=3)
etiket = Label(pencere,text="--")
etiket.grid(column=3,row=3)
########################################
def dosyaIcinAc():
    from tkinter import filedialog
    dosya = filedialog.askopenfilename(filetypes=(("Resim Dosyalari","*.png"),("Tüm Dosyalar","*.*")))
    print(dosya)
dugme4 = Button(pencere,text="Dosya için aç",command=dosyaIcinAc)
dugme4.grid(column=0,row=4)
pencere.mainloop()
from tkinter import *
from tkinter.ttk import *
pencere = Tk()
pencere.geometry("500x200+500+200")
##########################################
etiket = Label(pencere,text="Python'da ilk arayüz elemanım")
etiket.grid(column=0,row=0)
def tiklandi():
    etiket["text"] = "Tıkladı"

dugme = Button(pencere,text="Tıkla",command=tiklandi,width=15)
dugme.grid(column=1,row=0)
########################################
def tiklandi2():
    yazi = txt.get()
    etiket2.configure(text=yazi)
txt =Entry(pencere,width=15)
txt.grid(column=0,row=1)
dugme2 = Button(pencere,text="=>Aktar=>",command=tiklandi2)
dugme2.grid(column=1,row=1)
etiket2 = Label(pencere,text="--")
etiket2.grid(column=2,row=1)
######################################
def tiklandi3():
    secilmis = cmb.get()
    etiket3.configure(text=secilmis)
cmb = Combobox(pencere)
cmb.grid(column=0,row=2)
cmb["values"] = ("Seçiniz",1,2,3,4,5,"Yazi")
cmb.current(0)
dugme3 = Button(pencere,text="=>Aktar=>",command=tiklandi3)
dugme3.grid(column=1,row=2)
etiket3 = Label(pencere,text="--")
etiket3.grid(column=2,row=2)
#########################################
def tiklandi4():
    etiket4["text"] = chk_durum.get()
chk_durum = BooleanVar()
chk_durum.set(False)
chk = Checkbutton(pencere,text="Kabul Ediyorum",var=chk_durum)
chk.grid(column=0,row=3)
dugme4 = Button(pencere,text="=>Aktar=>",command=tiklandi4)
dugme4.grid(column=1,row=3)
etiket4 = Label(pencere,text="--")
etiket4.grid(column=2,row=3)
###############################################
def tiklandi5():
    etiket5.configure(text=secilmis.get())
secilmis = IntVar()
rdb1 = Radiobutton(pencere,text="Birinci",value=1,variable=secilmis)
rdb2 = Radiobutton(pencere,text="İkinci",value=2,variable=secilmis)
rdb3 = Radiobutton(pencere,text="Üçüncü",value=3,variable=secilmis)
rdb1.grid(column=0,row=4)
rdb2.grid(column=0,row=5)
rdb3.grid(column=0,row=6)
dugme5 = Button(pencere,text="=>Aktar=>",command=tiklandi5)
dugme5.grid(column=1,row=4)
etiket5 = Label(pencere,text="--")
etiket5.grid(column=2,row=4)
###############################################
def yeniPencere():
    from tkinter import  scrolledtext
    pencere2 = Tk()
    pencere2.geometry("500x500+300+300")
    txtSkrol = scrolledtext.ScrolledText(pencere2,width=50,height=20)
    txtSkrol.grid(column=0,row=0)
    txtSkrol.insert(INSERT,"Bizim Eklediğimiz Metin")
    def tikla():
        txtSkrol.delete(1.0, END)
    dugme = Button(pencere2,text="Silme",command=tikla)
    dugme.grid(column=0, row=1)
    pencere2.mainloop()
dugme6 = Button(pencere,text="Yeni Pencere",command=yeniPencere)
dugme6.grid(column=0,row=7)
pencere.mainloop()

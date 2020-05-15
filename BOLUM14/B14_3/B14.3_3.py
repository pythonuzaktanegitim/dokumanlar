from tkinter import *
from tkinter import  Menu,messagebox
pencere = Tk()
pencere.title("TK 14.3_3")
pencere.geometry("300x300+200+200")
def dosyaIcinAc():
    from tkinter import filedialog
    dosya = filedialog.askopenfilename(filetypes=(("Resim Dosyalari","*.png"),("Tüm Dosyalar","*.*")))
    print(dosya)
menu = Menu(pencere)
yeni_eleman = Menu(menu)
yeni_eleman.add_command(label="Yeni",command=dosyaIcinAc)
yeni_eleman.add_command(label="Düzenle",command=lambda :print("Düzenle"))
menu.add_cascade(label="Dosya",menu=yeni_eleman)
pencere.config(menu=menu)
from tkinter import  ttk
tab_kontrol = ttk.Notebook(pencere)
tab1 = ttk.Frame(tab_kontrol)
tab2 = ttk.Frame(tab_kontrol)
tab_kontrol.add(tab1,text="İlk")
tab_kontrol.add(tab2,text="İkinci")
dugme = Button(tab2,text="Tab 2 deyim")
dugme.grid(column=0,row=0)
tab_kontrol.pack(expand=1,fill="both")

pencere.mainloop()
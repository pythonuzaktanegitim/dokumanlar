class DosyaTool:
    def __init__(self,adres="defter.csv",**kwargs):
        self.adres = adres
        self.alanlar = ["Adı","Soyadı","Telefon"]
        for key,value in kwargs.items():
            if key == "alanlar":
                self.alanlar = value
        self.DosyaAc()
        self.liste = self.dosya.readlines()

    def DosyaAc(self):
        import os
        if os.path.exists(self.adres):
            self.dosya = open(self.adres, "r+", encoding="UTF-8")
        else:
            self.dosya = open(self.adres, "w+", encoding="UTF-8")

    def Listeleme(self):
        for i in range(len(self.liste)):
            kayit = ""
            for item in self.liste[i].split(";"):
                kayit += " "+ item
            satir = f"{i + 1}-{kayit}"
            print(satir,end="")

    def GirisYap(self):
        kayit = ""
        for item in self.alanlar:
            kayit += input(f"{item} Giriniz:") + ";"
        kayit = kayit.rstrip(";") + "\n"
        return kayit

    def KayitListele(self):
        self.Listeleme()

    def KayitEkle(self):
        self.liste.append(self.GirisYap())

    def KayitDuzelt(self):
        self.Listeleme()
        kayitNum = int(input("Güncellemek istediğiniz numarayı giriniz:"))
        self.liste[kayitNum - 1] = self.GirisYap()

    def KayitSil(self):
        self.Listeleme()
        kayitNum = int(input("Silmek istediğiniz numarayı giriniz:"))
        del self.liste[kayitNum - 1]

    def Menu(self):

        Menu = """
        1-Listeleme
        2-Ekleme
        3-Güncelleme
        4-Silme
        5-Çıkış
        İşlem Seçiniz:
        """

        anahtar = 1
        while anahtar == 1:
            print(self.adres,"konumundaki dosya üzerinde çalışılıyor")
            islem = input(Menu)
            if islem == "5":
                anahtar = 0
            elif islem == "1":
                self.KayitListele()
            elif islem == "2":
                self.KayitEkle()
            elif islem == "3":
                self.KayitDuzelt()
            elif islem == "4":
                self.KayitSil()
        else:
            self.dosya.seek(0)
            self.dosya.truncate()
            self.dosya.writelines(self.liste)
            self.dosya.flush()

    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(self.liste)
        self.dosya.close()

class BankaDefter(DosyaTool):
    def __init__(self,otomatikMenu=0):
        super().__init__("hesap.csv",alanlar=["Banka Hesap No","Tip","Tutar"],)
        if otomatikMenu : self.Menu()

class TelefonDefter(DosyaTool):
    def __init__(self,otomatikMenu=0):
        super().__init__("telefon.csv", alanlar=["Adı", "Soyadı", "Telefon"])
        if otomatikMenu : self.Menu()


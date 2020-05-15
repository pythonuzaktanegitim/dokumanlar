adres = "defter.csv"
alanlar = ["Adı","Soyadı","Telefon"]
liste = []
def DosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres, "w+", encoding="UTF-8")

def Listeleme(liste):
    for i in range(len(liste)):
        kayit = ""
        for item in liste[i].split(";"):
            kayit += item + " "
        satir = f"{i+1}-{kayit}"
        print(satir,end="")

def GirisYap():
    kayit = ""
    for item in alanlar:
        kayit += input(f"{item} Giriniz:") + ";"
    kayit = kayit.rstrip(";") + "\n"
    return kayit

def KayitListele(liste):
    Listeleme(liste)

def KayitEkle(liste):
    liste.append(GirisYap())

def KayitDuzelt(liste):
    Listeleme(liste)
    kayitNum = int(input("Güncellemek istediğiniz numarayı giriniz:"))
    liste[kayitNum-1] = GirisYap()

def KayitSil(liste):
    Listeleme(liste)
    kayitNum = int(input("Silmek istediğiniz numarayı giriniz:"))
    del liste[kayitNum-1]



def Menu():
    Menu = """
    1-Listeleme
    2-Ekleme
    3-Güncelleme
    4-Silme
    5-Çıkış
    İşlem Seçiniz:
    """

    dosya = DosyaAc(adres)
    liste = dosya.readlines()
    anahtar = 1
    while anahtar == 1:
        islem = input(Menu)
        if islem == "5":
            anahtar = 0
        elif islem == "1":
            KayitListele()
        elif islem == "2":
            KayitEkle(liste)
        elif islem == "3":
            KayitDuzelt(liste)
        elif islem == "4":
            KayitSil(liste)
    else:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()

if __name__ == "__main__":
    Menu()


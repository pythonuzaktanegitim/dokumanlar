def DosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")

def GirisAl():
    adi = input("Adını Giriniz:")
    soyadi = input("Soyadını Giriniz:")
    telefon = input("Telefonu Giriniz:")
    return adi + ";" + soyadi + ";" + telefon + "\n"

def KayitListele(liste):
    print("-" * 40)
    for i in range(len(liste)):
        adi, soyadi, telefon = liste[i].split(";")
        metin = f"{i + 1}-{adi} {soyadi} {telefon}"
        print(metin, end="")
    print("\n", "-" * 40, sep="")

def TelefonDefterMenu():
    dosya = DosyaAc(r"Defter.csv")
    menu = """
        1. Listele
        2. Ekle
        3. Sil
        4. Güncelle
        5. Çıkış
        İşlem Seçiniz :"""
    liste = dosya.readlines()
    anahtar = 1
    while anahtar == 1:
        islem = int(input(menu))
        if islem == 1:
            KayitListele(liste)
        elif islem == 2:
            liste.append(GirisAl())
        elif islem == 3:
            KayitListele(liste)
            kayitNum = int(input("Silmek istediğiniz kaydı seçiniz:"))
            liste.pop(kayitNum-1)
        elif islem == 4:
            KayitListele(liste)
            kayitNum = int(input("Güncellemek istediğiniz kaydı seçiniz:"))
            liste[kayitNum-1] = GirisAl()
        elif islem == 5:
            anahtar = 0
    else:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
        dosya.close()
if __name__=="__main__":
    TelefonDefterMenu()
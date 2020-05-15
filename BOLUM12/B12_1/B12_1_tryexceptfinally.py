def bölme():
    try:
        adim = "1A"
        sayi1 = int(input("1. Sayıyı Giriniz:"))
        adim = "2A"
        sayi2 = int(input("2. Sayıyı Giriniz:"))
        adim = "3A"
        sonuc = sayi1/sayi2
        adim = "4A"
        return sonuc
    except Exception as hata:
        return "Hata Var Hata Mesajı:"+str(hata)+"adim :"+adim
    finally:
        print("Blok Bitti")
print(bölme())
print("Devam Ediyor")
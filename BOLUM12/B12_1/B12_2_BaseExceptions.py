try:
    sayi1 = int(input("1. Sayıyı Giriniz:"))
    sayi2 = int(input("2. Sayıyı Giriniz:"))
    if sayi2 < 0:
        raise ZeroDivisionError
except ValueError:
    print("Sayı Girmeniz Gerekirdi")
except:
    print("Genel Hata Var")
else:
    try:
        sonuc = sayi1/sayi2
        print(sonuc)
    except ZeroDivisionError:
        print("İkinci Değer İçin Sıfır Girdiniz")

finally:
    print("iyi günler")



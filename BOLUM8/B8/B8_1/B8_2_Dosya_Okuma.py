def dosyaAc(adres):
    """
    :param adres: dosyanın adresi
    :return: dosya dönecek
    """
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="utf-8")
    else:
        return open(adres,"w+",encoding="utf-8")

dosya = dosyaAc(r"Defter1.txt")
# print(dosya.read())
#print(dosya.readline())
#print(dosya.readline())

liste = dosya.readlines()

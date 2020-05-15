def dosyaAc(adres):
    """
    :param adres: dosyanın adresi
    :return: dosya dönecek
    """
    import os
    if os.path.exists(adres):
        return open(adres,"r+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")

dosya = dosyaAc(r"Defter1.txt")
liste = ["Ali\n","ayşe\n","veli\n","Ali\n","ayşe\n","veli\n"]
dosya.writelines(liste)
dosya.flush()
dosya.write("yazmaya devam")
dosya.close()
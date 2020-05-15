def dosyaAc(adres):
    import os
    if os.path.exists(adres):
        return open(adres,"r+")
    else:
        return open(adres,"w")

dosya = dosyaAc(r"Telefon\Defter.csv")

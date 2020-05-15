class MarvelHero:
    import random as rnd
    def __init__(self,saglik,guc,isim):
        self.saglik = saglik
        self.guc = guc
        self.isim = isim
    def Vurus(self):
        return self.guc
    def SilahKullan(self):
        return self.guc*3
    def Darbe(self,guc):
        self.saglik -= guc
        return self.saglik
    def Kacinma(self,guc):
        return self.saglik
    def Savunma(self,guc):
        self.saglik -= guc/2
        return self.saglik
    def Ofans(self):
        fonk = rnd.choice([self.Vurus,self.SilahKullan])
        print(self.isim,fonk.__name__)
        return fonk()
    def Defans(self,guc):
        fonk = rnd.choice([self.Darbe,self.Kacinma,self.Savunma])
        print(self.isim, fonk.__name__)
        return fonk(guc)

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__(500,50,"Deadpool")
        self.super = 0

    def Darbe(self, guc):
        self.super += 1
        if self.super == 3:
            print(self.isim,"== Süper güç kullandı")
            self.saglik += 100
        else:
            self.saglik -= guc
        return self.saglik

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__(750,50,"Iron Man")
        self.super = 0

class KaptanAmerika(MarvelHero):
    def __init__(self):
        super().__init__(500,75,"Kaptan Amerika")
        self.super = 0

class Hulk(MarvelHero):
    def __init__(self):
        super().__init__(750,100,"Hulk")
        self.super = 0

    def Vurus(self):
        self.super += 1
        if self.super==5:
            print(self.isim,"== Süper güç kullandı")
            self.super = 0
            return self.guc*2
        else:
            return self.guc

import random as rnd
import time
liste = [Hulk,DeadPool,KaptanAmerika,IronMan]
P1 = rnd.choice(liste)()
P2 = rnd.choice(liste)()
print(f"P1 için {P1.isim} seçildi",f"P2 için {P2.isim} seçildi")
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(1)
    P2.Defans(P1.Ofans())
    print(f"{P1.isim}  ==> {P2.isim} vurdu ==> {P1.isim}:{P1.saglik} ve {P2.isim}:{P2.saglik}")
    time.sleep(1)
    P1.Defans(P2.Ofans())
    print(f"{P2.isim}  ==> {P1.isim} vurdu ==> {P1.isim}:{P1.saglik} ve {P2.isim}:{P2.saglik}")
else:
    if P1.saglik>P2.saglik:
        print(P1.isim,"Kazandı")
    else:
        print(P2.isim,"Kazandı")
    print("Oyun Bitti")


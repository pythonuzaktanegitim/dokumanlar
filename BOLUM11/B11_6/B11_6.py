from abc import abstractmethod


class Cokgen:
    @abstractmethod
    def KenarSayisi(self):
        pass
class Kare(Cokgen):
    def KenarSayisi(self):
        print("4 Kenarım Var")

class Ucgen(Cokgen):
    def KenarSayisi(self):
        print("3 Kenarım Var")

class Besgen(Cokgen):
    def KenarSayisi(self):
        print("5 Kenarım Var")

Sekil1 = Kare()
Sekil2 = Ucgen()
Sekil3 = Besgen()
Sekil1.KenarSayisi()
Sekil2.KenarSayisi()
Sekil3.KenarSayisi()



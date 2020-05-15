# class
class Kedi:
    pass

#class attribute
class Kedi:
    tur = "Ev Kedisi"
#class method
class Kedi:
    tur = "Ev Kedisi"
    @classmethod
    def KedininTuru(cls):
        return cls.tur
#constructor

#default constructor
class Kedi:
    tur = "Ev Kedisi"
    def __init__(self):
        print("Nesne Üretildi")
        self.ad = "Melek"

    @classmethod
    def KedininTuru(cls):
        return cls.tur
#parameterized constructor
class Kedi:
    tur = "Ev Kedisi"
    def __init__(self,ad):
        print("Nesne Üretildi")
        self.ad = ad

    @classmethod
    def KedininTuru(cls):
        return cls.tur
#destructor
class Kedi:
    tur = "Ev Kedisi"
    def __init__(self,ad):
        print("Nesne Üretildi")
        self.ad = ad

    def __del__(self):
        print("Rest In Peace")

    @classmethod
    def KedininTuru(cls):
        return cls.tur

#instance attribute
class Kedi:
    tur = "Ev Kedisi"

    def __init__(self, ad,yas):
        print("Nesne Üretildi")
        self.ad = ad
        self.yas = yas

    def __del__(self):
        print("Rest In Peace")

    @classmethod
    def KedininTuru(cls):
        return cls.tur

#instance method

class Kedi:
    tur = "Ev Kedisi"

    def __init__(self, ad,yas):
        self.ad = ad
        self.yas = yas

    def Beslen(self):
        print(self.ad,"Beslendi")


    @classmethod
    def KedininTuru(cls):
        return cls.tur

#instantiation
Melek = Kedi("Melek",5)
Pamuk = Kedi("Pamuk",4)
Pamuk.Beslen()
print(Kedi.KedininTuru())
print(Melek.KedininTuru())
print(Pamuk.KedininTuru())



# encapsulation


#semi private attributes
class A:
    def __init__(self):
        self.a = "Normal"
        self._b ="Korulmalı"

class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._b)

Nesne = A()
Nesne1 = B()
print(Nesne1._b)


#private attributes
class A:
    def __init__(self):
        self.a = "Normal"
        self._b = "Korumalı"
        self.__c = "Gizli"

class B(A):
    def __init__(self):
        self.b = "Normal"
        A.__init__(self)

Nesne = A()
Nesne1 = B()




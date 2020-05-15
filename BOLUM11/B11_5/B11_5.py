#builtin polymorphic functions
metin = "Python Eğitimi"
print(len(metin))
liste = ["1",1,2,3]
print(len(liste))
#user defined polymorphic functions
def fonk(a,b,c=0):
    return a+b+c
print(fonk(1,2))
print(fonk(1,2,3))
#Polymorphism with class methods
class Ulke1():
    def yer():
        print("Ulke1 Asya Kıtasındadır.")
    def nufus():
        print("Ulke1 Nufus 200 Milyon")
    def type():
        print("Federal Cumhuriyet")
class Ulke2():
    def yer():
        print("Ulke2 Avrupa Kıtasındadır.")
    def nufus():
        print("Ulke2 Nufus 50 Milyon")
    def type():
        print("Cumhuriyet")

def Fonk(nesne):
    nesne.yer()
    nesne.nufus()
    nesne.type()

for item in (Ulke1,Ulke2):
    Fonk(item)
#Polymorphism with Inheritance
class A:
    def fonk1(self):
        print("A üzerinden çalıştı")
class B(A):
    def fonk1(self):
        print("B üzerinden çalıştı")
        super(A, self).fonk1()
class C(B):
    def fonk1(self):
        print("C üzerinden çalıştı")
        super(B,self).fonk1()

for item in (A,B,C):
    item().fonk1()
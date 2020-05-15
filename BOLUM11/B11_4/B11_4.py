class A:
    def __init__(self):
        self.a = "A sınıfına ait örnek özellik"
    def soyleA(self):
        print("Söyle A çalıştı")
class A_1:
    def __init__(self):
        self.a_1 = "A1 sınıfına ait örnek özellik"
    def soyleA_1(self):
        print("Söyle A_1 çalıştı")

class B(A,A_1):
    def __init__(self):
        A.__init__(self)
        A_1.__init__(self)
        print(self.a)
        self.b = "B Sınıfına ait örnek özellik"

class C(B):
    def __init__(self):
        super().__init__()


nesneA = A()
nesneA_1 = A_1()
nesneB = B()
nesneC = C()
print(type(nesneA))
print(type(nesneB))
print(type(nesneC))
print(isinstance(nesneA,C))
print(issubclass(C,B))
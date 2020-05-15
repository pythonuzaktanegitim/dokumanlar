

import math
def GeneratFonk(a):
    i = 0
    while i<=a:
        yield math.factorial(i)
        i+=1

for j in GeneratFonk(10):
    print(j)

import random as rnd
def GeneratorFonk():
    liste = [i for i in range(1, 50)]
    sonuc = rnd.sample(liste,6)
    for i in sonuc:
        yield i
def LotoOyna(KolonSay=1):
    for i in range(KolonSay):
        liste = []
        for j in GeneratorFonk():
            liste.append(j)
        liste.sort()
        yield liste

for kolon in LotoOyna(5):
    print(kolon)

def GenFonk():
    yield 1
    yield 2
    yield 3

x = GenFonk()
print(x.__next__())
print(x.__next__())
print(x.__next__())
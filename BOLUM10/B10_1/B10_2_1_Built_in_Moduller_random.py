import random as rnd
liste = [1,2,3,4,5,6,7,8,9,10]
liste = ["Ahmet","Ayşe","Fatma","Hakkı","Soner","Işıl"]
#print(rnd.choice(liste))
print(rnd.sample(liste,3))
print(rnd.choices(liste,k=3))

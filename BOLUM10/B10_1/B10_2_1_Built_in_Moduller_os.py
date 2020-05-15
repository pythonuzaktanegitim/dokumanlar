import os
#print(os.getcwd())
#print(os.sep)
#yol = os.getcwd() + os.sep + r"Telefon\Defter.csv"
#print(yol)
#dosya = open(os.getcwd() + os.sep + r"Telefon\Defter.csv")
#print(*dosya.readlines())
print(os.getcwd())
os.chdir("D:\Paket")
print(os.getcwd())
for dosya in os.walk(os.curdir):
    print(f"Mevcut Yer:{dosya[0]}")
    print("Klasör Listesi",*dosya[1])
    print("Dosya Listesi", *dosya[2])
print(os.path.exists(os.getcwd() + os.sep + r"Telefon\Defter.csv"))
print(os.path.isfile(os.getcwd() + os.sep + r"Telefon\Defter.csv"))
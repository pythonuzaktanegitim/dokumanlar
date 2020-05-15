
rakamlar = {"0":["1","1","1","1","1","1","0"],
            "1":["0","1","1","0","0","0","0"],
            "2":["1","1","0","1","1","0","1"],
            "3":["1","1","1","1","0","0","1"],
            "8":["1","1","1","1","1","1","1"]}

satir1 = satir2 = satir3 = satir4 = satir5 = ""
def Rakamlar(yazilan):
    global  satir1,satir2,satir3,satir4,satir5
    for rakam in yazilan:
        for i in range(len(rakamlar[rakam])):
            liste = rakamlar[rakam]
            if liste[i]  == "1":
                liste[i] = "*"
            else:
                liste[i] = " "
            rakamlar[rakam] = liste

        a,b,c,d,e,f,g = rakamlar[rakam]
        satir1 += f"{f} {a} {b}\t"
        satir2 += f"{f}   {b}\t"
        satir3 += f"{f} {g} {b}\t"
        satir4 += f"{e}   {c}\t"
        satir5 += f"{e} {d} {c}\t"


Rakamlar("01823")
print(f"""
    {satir1}
    {satir2}
    {satir3}
    {satir4}
    {satir5}
    """)
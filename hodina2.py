def scitaj(a, b):
    print(a + b)

def funkcia():
    print("Zaciatok funkcie")
    scitaj(7, 2)
    print("Koniec funkcie")

##funkcia()
##funkcia()
##funkcia()
##funkcia()

def pozdrav(meno):
    print("Ahoj", meno)

##pozdrav("Fero")

def opakuj(pocet, slovo):
    for i in range(pocet):
        print(slovo)
    print("test")

##opakuj(4, "Ahoj")

# funkcia s menom poradie, s 1 parametrom n
# vypise cisla od 1 po n
def poradie(n):
    for i in range(n):
        print(i+1)
        print("test:",i)

##poradie(10)

##for i in [7,25,1,48,17]:
##    print(i)


##zoznam = [1,3,7, "Ahoj", 7.6]
##zoznam2 = [7,5,2]
##print(zoznam)
##print(zoznam[3])
##zoznam.append(4)
##
##for i in zoznam2:
##    zoznam.append(i)
##
##print(zoznam)
##print(zoznam[6])

def moj_range(zaciatok, koniec, krok):
    pole = []
    for i in range(zaciatok, koniec+1, krok):
        pole.append(i)
    return pole

print(moj_range(4,7,1))

moje_pole = moj_range(4,7,1)
moje_pole.append(48)
print(moje_pole)

##for i in moj_range(4,7,1):
##    print(i)
        

pole = [787,67,867334,88,4,383,434,384,843,834,43]
pole.sort()
print(pole)

def stvorec(a):
    for i in range(a):
        for j in range(a):
            print("#", end="")
        print()

def lahsi_stvorec(a):
    for i in range(a):
        print("#" * a)

stvorec(7)
lahsi_stvorec(3)


for i in range(10):
    print("Ahoj")
    if i == 7:
        continue
    print(i)

text = "Ahoj ako sa mas ?"
for i in range(len(text)):
    print(text[i])
    
for i in text:
    print(i)

print(text[0])
print(text[0:7])
print(text[0:7:2])
print(text[4:])
print(text[:7])

sifra = "Anhkokjl"
print(sifra[::2])

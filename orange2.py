##pole = [1,2,3,4,5]
##prazdnepole = []
##
##i = input("Zadaj cislo: ")
##j = input("Zadaj cislo2: ")
##k = input("Zadaj cislo3: ")
##l = input("Zadaj cislo4: ")
##m = input("Zadaj cislo5: ")
##
##prazdnepole.append(i)
##prazdnepole.append(j)
##prazdnepole.append(k)
##prazdnepole.append(l)
##prazdnepole.append(m)

##prazdnepole = []
##
##for i in range(5):
##    prazdnepole.append(input("Zadaj cislo: "))
##
##print(prazdnepole[0])

##print([1,2,3] + [4,5])


##from random import randint
##
##cisla = []
##for i in range(20):
##    cisla.append(randint(1,100))
##
##print(cisla)
##
##for cislo in cisla:
##    if cislo % 2 == 1:
##        print(cislo)
##
##pocitadlo = 0
##while pocitadlo < len(cisla):
##    if cisla[pocitadlo] %2 == 0:
##        print(cisla[pocitadlo])
##        
##    pocitadlo += 1
    
##from random import randint
##
##hody = []
##vysledky = [0,0,0,0,0,0]
##je = 0
##dv = 0
##tr = 0
##st = 0
##pa = 0
##se = 0
##for i in range(20):
##    hod = randint(1,6)
##    hody.append(hod)
##    vysledky[hod-1] += 1
##    if hody[i] == 1:
##        je += 1
##    if hody[i] == 2:
##        dv += 1
##    if hody[i] == 3:
##        tr += 1
##    if hody[i] == 4:
##        st += 1
##    if hody[i] == 5:
##        pa += 1
##    if hody[i] == 6:
##        se += 1
##    
##    
##print(hody)
##
##print("1: ", je)
##print("2: ", dv)
##print("3: ", tr)
##print("4: ", st)
##print("5: ", pa)
##print("6: ", se)
##
##print(vysledky)
##pocitadlo = 1
##for vysledok in vysledky:
##    print(pocitadlo, ":" + str(vysledok))
##    pocitadlo += 1
##
##
##vysledky = [0, 0, 0, 0, 0, 0]
##
##for i in range(20):
##    hod = randint(0,5)
##    vysledky[hod] += 1
##    print(vysledky)
##
##print(vysledky)
##pocitadlo = 1
##for vysledok in vysledky:
##    print(pocitadlo, ":" + str(vysledok))
##    pocitadlo += 1

##from random import randint
##
##hrac = 0
##pc = 0
##
##while hrac < 3 and pc < 3:
##    volba = input("Zadaj kamen papier alebo noznice: ")
##    znak = 0
##    if volba == "kamen":
##        znak = 1
##    elif volba == "papier":
##        znak = 2
##    elif volba == "noznice":
##        znak = 3
##    else:
##        print("zla volba")
##        continue
##    znakPC = randint(1,3)
##    if znak == znakPC:
##        print("remiza")
##    elif (znak == 1 and znakPC == 3 or
##          znak == 2 and znakPC == 1 or
##          znak == 3 and znakPC == 2):
##        print("vyhral si")
##        hrac += 1
##    else:
##        print("prehral si")
##        pc += 1
##
##    print("hrac : Pc")
##    print(hrac, ":", pc) 

##from random import randint
##
##def generuj():
##    cisla = []
##    while sum(cisla) != 1000:
##        if sum(cisla) > 1000:
##            cisla.pop()
##        cislo = randint(1,100)
##        cisla.append(cislo)
##    print(cisla)
##    print(sum(cisla))
##    
##generuj()


##from random import randint
##pole1 = []
##pole2 = []
##
##for i in range(10):
##    pole1.append(randint(1,100))
##    pole2.append(randint(1,100))
##
##
##print(pole1)
##print(pole2)
##print()
##pole3 = []
##for i in range(10):
##    pole3.append(pole1[i]+pole2[i])
##
##print(pole3)


##from random import randint
##
##cislo = 3**6000
##
##
##def jePrvocislo(a):
##    for i in range(2, a):
##        if a % i == 0:
##            return False
##    return True
##
##print(cislo, jePrvocislo(cislo))


from random import randint

pole = []

for i in range(randint(10,50)):
    pole.append(randint(1,100))

cislo = int(input("Zadaj cislo: "))
while cislo > len(pole):
    print("Zadaj mensie cislo")
    cislo = int(input("Zadaj cislo: "))
    
pole.sort()

print(pole)
print(pole[len(pole)-cislo])















    

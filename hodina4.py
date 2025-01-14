##print("Ahoj programujem")
##print("4+5")
##print(4+5)
##ahoj = "Ahoj ako sa mas ?"
##print(ahoj)

##cislo = input("Zadaj slovo: ")
##print(cislo)

##input()
##print("ahoj", end="")
##print("Jano")
##print("Ahoj", "ako", "sa", "mas", "?")
##print("Ahoj", "ako", "sa", "mas", "?", sep="-")
##print()
##print("Ahoj", "ako", "sa mas", "?", sep="-")

##cislo1 = int(input("Zadaj cislo: "))
##cislo2 = int(input("Zadaj cislo: "))
##
##if cislo1 > cislo2:
##    print("1. cislo je vacsie")
##elif cislo1 == cislo2:
##    print("cisla sa rovnaju")
##else:
##    print("2. cislo je vacsie")
##
##print(7+7)
##print(cislo1+cislo2)

##text = "ahoj ako sa mas ?"          #string
##cislo = 7                           #integer int
##des_cislo = 7.0                     #float
##pravdivostna_hodnota = True         #bool
##
##print(7+7)
##print(7-7)
##print(7*7)
##print(7/7)
##print(13//7)        #celociselne delenie
##print(5%2)          #zvysok po deleni
##print(2**8)         #umocnovanie


##for i in range(10):
##    print("ahoj")
##    print("nieco")
##print("tu je koniec cyklu")
##
##for i in range(10):
##    print(i)
##print()
##for i in range(3,10):
##    print(i)
##print()
##for i in range(1,10,2):
##    print(i)

##cislo = 0
##
##while cislo < 7:
##    cislo += 1 # cislo = cislo + 1
##    print(cislo)
##
####slovo = input("Zadaj slovo Ahoj: ")
####
####while slovo != "Ahoj":
####    print("Zadal si zle slovo")
####    slovo = input("Zadaj slovo: ")
####
####print(slovo)
##print()
##cislo1 = 0
##while cislo1 < 7:
##    print(cislo1)
##    if cislo1 == 3:
##        cislo1 += 3
##    else:
##        cislo1 +=1
##    if cislo1 == 4:
##        break
##          
##print()
##cislo1 = 0
##while cislo1 < 7:
##    print(cislo1)
##    if cislo1 == 3:
##        cislo1 += 3
##        
##    cislo1 +=1

##from random import randint
##
##hadane_cislo = randint(1, 10)
##
##pokus = int(input("Hadaj na ake cislo myslim: "))
##while pokus != hadane_cislo:
##    print("Netrafil si sa")
##    pokus = int(input("Hadaj na ake cislo myslim: "))
##
##print("Huraaa trafil si sa!!!")

##pole = [7,12,4,5,6,8,7,1,2,2549856526868,"text"]
##
##print(pole)
##print(pole[3])
##print(len(pole))
##pole.append(256)
##print(pole)
##
##for i in range(0, len(pole), 1):
##    print(pole[i])
##
##pocitadlo = 0
##
##while pocitadlo < len(pole):
##    print(pole[pocitadlo])
##    pocitadlo += 1

pole = [1,5,3,-2,7,4]

maximalne_cislo = pole[0]
for i in range(len(pole)):
    if maximalne_cislo < pole[i]:
        maximalne_cislo = pole[i]

print(maximalne_cislo)


minimalne_cislo = pole[0]

pocitadlo = 0
while pocitadlo < len(pole):
    if minimalne_cislo > pole[pocitadlo]:
        minimalne_cislo = pole[pocitadlo]
    pocitadlo += 1

print(minimalne_cislo)

print(max(pole))
print(min(pole))

pole.sort()

print(pole)
print(sum(pole))

sucet = 0
for i in range(len(pole)):
    sucet += pole[i]
print(sucet)

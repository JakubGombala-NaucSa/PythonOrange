ahoj = "Ako sa mas ?"
print(ahoj)

# Tu sa pýtame na meno užívateľa
slovo = input("Zadaj meno: ")
print("Ahoj", slovo)    # Výpis cez čiarku
print("Ahoj " + slovo)  # Sčítavanie textov
print()                 # Prázdny riadok

slovo = "text"      #string  (str)
cislo = 7           #integer (int)
descislo = 7.0      #float   (float)
pravdhodnota = True #boolean (bool)

print(4+5) 
print(4-5)
print(4*5)
print(4/5)
print(4//5) # Celočíselné delenie
print(4%5)  # Zvyšok po delení
print(4**5) # Umocňovanie

print("Ahoj", end=" ") # Nepovinný parameter end
print("Jakub")
print("nieco")

print("slovo","slovo1","slovo2")
print("slovo","slovo1","slovo2", sep="-") # Nepovinný parameter sep (separátor)
print("slovo","slovo1","slovo2")

# -------------------------------------
# ------------- Podmienky -------------
# -------------------------------------
if 4 < 5:
    print("pravda")
    print("Ahoj")
    
if 25 > 10:         # Vetva 1
    print("jedna")
elif 7 > 4:         # Vetva 2
    print("dva")
elif 22 < 33:       # Vetva 3
    print("tri")
else:               # Vetva else
    print("nepravda")

print("Ja uz nie som v podmienke")


slovo = input("Zadaj slovo: ")
if slovo == "voldemort":
    print("pssst, toto meno sa nesmie vypisovat")

cislo1 = int(input("zadaj cislo1: "))
cislo2 = int(input("zadaj cislo2: "))

if cislo1 > cislo2:
    print("Prve cislo je vacsie")
elif cislo1 == cislo2:
    print("Cisla sa rovnaju")
else:
    print("Druhe cislo je vacsie")
    
# -------------------------------------
# --------------- Cykly ---------------
# -------------------------------------

for i in range(10):         # Koncové číslo (vždy o 1 menšie)
    print(i)
for i in range(3, 10):      # Začiatočné a koncové čísla
    print(i)
for i in range(3, 10, 2):   # Začiatočné, koncové čisla a krok
    print(i)

sucet = 0
for nieco in range(11):
    sucet = sucet + nieco
    print(sucet)
print(sucet)

sucin = 1
for nieco in range(1,11):
    sucin = sucin * nieco
    print(sucin)
print(sucin)

for i in range(3):
    print("tento kod je vo vnutri")
    print("tento kod je vo vnutri tiez")

    for j in range(2): # Vnorený cyklus
        print("Ahoj")
        
print("koniec")


for i in range(3):
    print(i)
    for i in range(2):
        print(i)

from random import randint # použitie knižnice na generovanie náhodných čísiel
nahodne_cislo = randint(1,10) # generovanie náhodného celého čísla od 1 do 10
##print(nahodne_cislo)

print("Hadaj nahodne cislo")
for i in range(3):
    pokus = int(input("Pokus " + str(i + 1) + ": "))
    if nahodne_cislo == pokus:
        print("Uhadol si")
        break # Zastaví (rozbije) cyklus
    else:
        print("Neuhadol si")
print("koniec")















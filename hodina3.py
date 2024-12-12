##text = "Ahoj ako sa mas?"
##for i in range(len(text)):
##    print(text[0:i+1])
##    
##print(text[0:4])
##print("a"*7)

def odznak(meno):
    for i in range(len(meno)+4):
        print("*", end="")
    print()
    
    print("*", end="")
    for i in range(len(meno)+2):
        print(" ", end="")
    print("*")

    print("* ", end="")
    print(meno, end="")
    print(" *")

    print("*", end="")
    for i in range(len(meno)+2):
        print(" ", end="")
    print("*")

    for i in range(len(meno)+4):
        print("*", end="")
    print()

def odznak2(meno):
    print("*"*(len(meno)+4))
    print("*" + " "*(len(meno)+2)+"*")
    print("*", meno, "*")
    print("*" + " "*(len(meno)+2)+"*")
    print("*"*(len(meno)+4))
        
##odznak("ema")
##odznak2("Jano")
# *******
# *     *
# * ema *
# *     *
# *******

##text = input("Zadaj text: ")
##pocet = int(input("Zadaj pocet hlasok: "))
##if len(text) < pocet:
##    print("Text je prilis kratky")
##else:
##    print(text[0:pocet])


def najdi(znak, veta):
    for i in range(len(veta)):
        if znak == veta[i]:
            return True
    return False

##print(najdi("a", "ahoj"))
##print(najdi("b", "ahoj"))

def najdiSlovo(slovo, veta):
    for i in range(len(veta)):
        if slovo == veta[i:i+len(slovo)]:
            return True
    return False

print(najdiSlovo("ahoj", "ahoj ako sa dnes mas ?"))
print(najdiSlovo("sa", "ahoj ako sa dnes mas ?"))

text = "ahoj ako sa dnes mas ?"
print(text[5:3])







        




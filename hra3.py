import tkinter as tk

root = tk.Tk()
root.title("Meno hry")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

doska = platno.create_rectangle(180, 560, 220, 580, fill="brown")

def sipkaVlavo(event):
    koordinaty = platno.coords(doska)
    if koordinaty[0] > 0:
        platno.move(doska, -20, 0)

def sipkaVpravo(event):
    koordinaty = platno.coords(doska)
    if koordinaty[2] < 400:
        platno.move(doska, 20, 0)

root.bind("<Left>", sipkaVlavo)
root.bind("<Right>", sipkaVpravo)

gulicka = platno.create_oval(20, 20, 40, 40, fill="red")

def Start():
    Animacia()

def Animacia():
    global gulicka
    platno.move(gulicka, 0, 20)
    koordinaty = platno.coords(gulicka)
    if koordinaty[3] > 600:
        return

    platno.after(100, Animacia)

Start()
root.mainloop()



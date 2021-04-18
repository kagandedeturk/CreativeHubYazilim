
from tkinter import *

def tl_dolar():
    tl = float(tl_input.get())
    dolar = round(tl / 8.07, 2)
    dolar_deger.config(text = f"{dolar}")

def dolar_tl():
    dolar = float(dolar_input.get())
    tl = round(dolar * 8.07, 2)
    tl_deger.config(text = f"{tl}")

ekran = Tk()
ekran.title("Para Birimi Donusturucu")
ekran.config(padx=20, pady=20)
ekran.minsize(width=500, height=400)


tl_input = Entry(width=7)
tl_input.grid(row=0, column=0)

tl_label = Label(text="TL")
tl_label.grid(row=0, column=1)

esittir = Label(text = "=")
esittir.grid(row=0, column=2)

dolar_deger = Label(text="0")
dolar_deger.grid(row=0,column=3)

dolar_isaret = Label(text="$")
dolar_isaret.grid(row=0, column=4)

hesapla_buton = Button(text="Donustur", command = tl_dolar)
hesapla_buton.grid(row=0, column = 6)

dolar_input = Entry(width=7)
dolar_input.grid(row=1,column = 0)

dolar_label = Label(text="$")
dolar_label.grid(row=1, column=1)

esittir2 = Label(text = "=")
esittir2.grid(row=1, column=2)

tl_deger = Label(text="0")
tl_deger.grid(row=1,column=3)

tl_label2 = Label(text="TL")
tl_label2.grid(row=1, column=4)

hesapla_buton2 = Button(text="Donustur", command = dolar_tl)
hesapla_buton2.grid(row=1, column = 6)



ekran.mainloop()
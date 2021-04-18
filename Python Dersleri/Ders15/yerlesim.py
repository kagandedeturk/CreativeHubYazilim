
# import tkinter as tk

from tkinter import *


# Yerlesim yontemleri: Pack, Place, Grid


ekran = Tk()
ekran.title("Yerlesim Yontemleri")
ekran.minsize(width = 500, height = 400)
# ekran.config(padx=100,pady=100)


#Label - etiket
etiket = Label(text="Etiket - 1",font=("Arial",18,"bold"))

etiket.config(text="Etiketim")
# etiket.pack(side="left")

# etiket.place(x=100,y=100)

etiket.grid(column=0,row=0)


# # #Label - etiket
# etiket2 = Label(text="Etiket - 2",font=("Arial",18,"bold"))
# # # etiket.pack()
# # etiket2.pack(side="left")
# etiket2.grid(row=1,column=1)

def buton_tiklandi():
    print("Buton tiklandi")
    metin = girdi.get()
    # print(metin)
    etiket.config(text = metin)


buton = Button(text="Tikla", command=buton_tiklandi)
buton.grid(row=1,column=1)

buton2 = Button(text = "Yeni Buton")
buton2.grid(row=0,column=2)


girdi = Entry(width=20)

girdi.grid(row=2, column=3)


ekran.mainloop()
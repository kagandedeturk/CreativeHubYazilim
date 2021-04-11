
# tkinter ---> Graphical User Interface ---> GUI

# import tkinter
# import tkinter as tk
from tkinter import *

# Yeni bir ekran olusturma ve o ekranin ozelliklerini tanimla

ekran = Tk()
ekran.title("TK Giris Dersi") # Ekrana baslik ismi verme
ekran.minsize(width = 500, height = 500)
#ekran.maxsize(width = 800, height = 500)


# Labels - Etiketler
etiket = Label(text = "1. etiket")
etiket.config(text = "1. etiket duzenlendi")
etiket.pack()



# buton olusturma
def buton_calistir():
    print("Butona tiklandi")


buton = Button(text = "Tikla", command = buton_calistir)
buton.pack()



# Entries --> Metin kutusu --> textbox
metin_kutusu = Entry(width=30)
metin_kutusu.insert(END, string="Eklenecek Metin")
print(metin_kutusu.get())
metin_kutusu.pack()


# Metin kutusu
metin = Text(height = 5, width = 25)
metin.focus() # Metin kutusunun icine cursor olusturur
metin.insert(END, "Metin-1")
metin.pack()




# Scale
def olcek_calistir(deger):
    print(deger)

olcek = Scale(from_= -100, to = 100, command = olcek_calistir)
olcek.pack()




#Spinbox



ekran.mainloop() # Ekranin acik kalmasini saglar


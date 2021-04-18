
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

def spinbox_kullan():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width = 5, command=spinbox_kullan)
spinbox.pack()


# Cek kutusu

def cek_kutusu_kullan():
    print(durum.get())

durum = IntVar()
cek = Checkbutton(text="Secili mi?", variable = durum, command=cek_kutusu_kullan)
cek.pack()


# Radio Buton



def radio_kullan():
    print(radio_degerleri[radio_durum.get()])

radio_degerleri = {
    1 : "Secenek-1",
    2 : "Secenek-2"
}


radio_durum = IntVar()
radio1 = Radiobutton(text="Secenek-1", value = 1, variable = radio_durum, command = radio_kullan)
radio2 = Radiobutton(text="Secenek-2", value = 2, variable = radio_durum, command = radio_kullan)
radio1.pack()
radio2.pack()


#Listbox - Liste Kutusu
def liste_kutusu_kullan(olay):
    print(liste_kutusu.get(liste_kutusu.curselection()))

renkler = ["Sari", "Kirmizi", "Siyah","Beyaz","Yesil"]
liste_kutusu = Listbox(height = len(renkler))
for item in renkler:
    liste_kutusu.insert(renkler.index(item),item)
liste_kutusu.bind("<<ListboxSelect>>",liste_kutusu_kullan)
liste_kutusu.pack()


# radio_degerleri = ["Secenek-1","Secenek-2"]

ekran.mainloop() # Ekranin acik kalmasini saglar


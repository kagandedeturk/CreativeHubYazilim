from tkinter import *
import random as rnd


# ------------------------------------SIFRE_URETME-------------------------------

def sifre_uret():
    
    harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numaralar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    
    # sifre_harfleri = []
    # for _ in range(rnd.randint(6,9)):
    #     sifre_harfleri.append(rnd.choice(harfler))

    sifre_harfleri = [rnd.choice(harfler) for i in range(rnd.randint(6,9))]
    sifre_numaralar = [rnd.choice(numaralar) for i in range(rnd.randint(2,5))]
    sifre_semboller = [rnd.choice(semboller) for i in range(rnd.randint(2,5))]

    sifre_listesi = sifre_harfleri + sifre_numaralar + sifre_semboller
    rnd.shuffle(sifre_listesi)

    sifre = ""

    for harf in sifre_listesi:
        sifre += harf

    sifre_entry.insert(0,sifre)

    
   









#---------------------------------------GUI---------------------------------------

ekran = Tk()
ekran.title("Sifre Uret")

ekran.config(padx= 50, pady= 50)


canvas = Canvas(height = 150, width = 150)

logo_img = PhotoImage(file="lock.png")
canvas.create_image(75, 75, image = logo_img)
canvas.grid(row=0,column=1)


#Etiketler
site_label = Label(text = "Web Sitesi: ",font=("Arial",12,"bold"))
site_label.grid(row=1, column = 0)
eposta_label = Label(text = "Eposta/KullaniciAdi: ",font=("Arial",12,"bold"))
eposta_label.grid(row=2, column = 0)
sifre_label = Label(text = "Sifre: ",font=("Arial",12,"bold"))
sifre_label.grid(row=3, column = 0)

#Metin Kutulari
site_entry = Entry(width = 42)
site_entry.grid(row=1, column=1, columnspan=2) # columnspan degeri kac adetse o kadar sutunu kaplar

eposta_entry = Entry(width = 42)
eposta_entry.grid(row=2, column=1, columnspan=2)

sifre_entry = Entry(width = 32)
sifre_entry.grid(row=3, column=1)


# Butonlar

sifre_uret_butonu = Button(text = "Sifre Uret",command = sifre_uret)
sifre_uret_butonu.grid(row=3,column=2)

kaydet_buton = Button(text="Kaydet",width= 36)
kaydet_buton.grid(row=4,column=1, columnspan = 2)



ekran.mainloop()
#Şifre Üretme Projesi
import random
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numaralar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre Üretme Programı")
harf_sayisi= int(input("Şifreniz kaç adet harf içersin istiyorsunuz? ")) 
sembol_sayisi = int(input("Kaç adet sembol içersin istiyorsunuz? "))
numara_sayisi = int(input("Kaç adet numara içersin istiyorsunuz? "))

#Kolay Seviye - Karakterlerin sırası random değil:
#ör: 4 harf, 2 sembol, 2 numara = JduE&!91

#Zor Seviye - Karakterlerin sırası random:
#ör: 4 harf, 2 sembol, 2 numara = g^2jk8&P
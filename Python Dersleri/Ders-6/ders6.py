
#Şifre Üretme Projesi
import random as rnd
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numaralar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre Üretme Programı")
harf_sayisi = int(input("Şifreniz kaç adet harf içersin istiyorsunuz? ")) 
sembol_sayisi = int(input("Kaç adet sembol içersin istiyorsunuz? "))
numara_sayisi = int(input("Kaç adet numara içersin istiyorsunuz? "))

# Kolay Seviye - Karakterlerin sırası random değil:
# ör: 4 harf, 2 sembol, 2 numara = JduE&!91

# Zor Seviye - Karakterlerin sırası random:
# ör: 4 harf, 2 sembol, 2 numara = g^2jk8&P


# Kolay Seviye şifre üretme
sifre = ""

for i in range(harf_sayisi):
    sifre += harfler[rnd.randint(0,len(harfler)-1)]


for i in range(harf_sayisi):
    sifre = sifre + rnd.choice(harfler)
for i in range(sembol_sayisi):
    sifre += rnd.choice(semboller)
for i in range(numara_sayisi):
    sifre += rnd.choice(numaralar)

print(f"Sifreniz: {sifre}")



# Zor seviye şifre üretme
sifre = []

for i in range(harf_sayisi):
    sifre.append(rnd.choice(harfler))
for i in range(sembol_sayisi):
    sifre.append(rnd.choice(semboller))
for i in range(numara_sayisi):
    sifre.append(rnd.choice(numaralar))

# Karistirmadan once
print(sifre)

# Karistirdiktan sonra
rnd.shuffle(sifre)
print(sifre)

str_sifre = ""
for karakter in sifre:
    str_sifre += karakter

print(f"Sifreniz: {str_sifre}")




'''
Geçen ders yazdığımız taş kağıt makas oyununu klavyeden -1 girilinceye kadar tekrarlayan
-1 girilince tekrar sormayan şekilde güncelledik
while döngüsü kullanarak kullanıcı -1 girinceye kadar kullanıcının oyuna devam etmesini sağladık.
'''

# Taş, Kağıt, Makas oyunu...
# Kullanıcıdan Taş, Kağıt veya Makastan birini seçmesi istenir. 
# Bilgisayarda Taş, Kağıt veya Makastan rastgele bir şekilde birini seçer

import random   #random modülünü programımıza ekleme

tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


liste = [tas, kagit, makas]

print("Tas Kagit Makas oyununa hos geldiniz...")
secim = int(input("Tasi secmek icin 0, kagidi secmek icin 1, makasi secmek icin 2 ve çıkmak için -1 giriniz: "))

while secim != -1:

    if secim == 0 or secim == 1 or secim == 2:

        bilgisayar_secim = random.randint(0,2)

        print(f"Sizin seciminiz:\n{liste[secim]}")

        print(f"Bilgisayarin secimi:\n{liste[bilgisayar_secim]}")   

        if secim == 0:
            if bilgisayar_secim == 0:
                print("Berabere")
            elif bilgisayar_secim == 1:
                print("Bilgisayar kazandi")
            elif bilgisayar_secim == 2:
                print("Kazandiniz")
        elif secim == 1:
            if bilgisayar_secim == 0:
                print("Kazandiniz")
            elif bilgisayar_secim == 1:
                print("Berabere")
            elif bilgisayar_secim == 2:
                print("Bilgisayar Kazandi")
        elif secim == 2:
            if bilgisayar_secim == 0:
                print("Bilgisayar kazandi")
            elif bilgisayar_secim == 1:
                print("Kazandiniz")
            elif bilgisayar_secim == 2:
                print("Berabere")

    secim = int(input("Tasi secmek icin 0, kagidi secmek icin 1, makasi secmek icin 2 ve cikmak icin -1 giriniz: "))






# İç içe döngüler

for i in range(1,6):
    print(f"i = {i}")
    for j in range(1,11):
        print(f"j = {j}", end = " ") # end = " " yan yana bir boşlukla yazmamızı sağlıyor
    print("")


# Yukarıdaki iç içe for döngüsü aşağıda görülen çıktıyı bize verir.
'''
i = 1
j = 1 j = 2 j = 3 j = 4 j = 5 j = 6 j = 7 j = 8 j = 9 j = 10 
i = 2
j = 1 j = 2 j = 3 j = 4 j = 5 j = 6 j = 7 j = 8 j = 9 j = 10 
i = 3
j = 1 j = 2 j = 3 j = 4 j = 5 j = 6 j = 7 j = 8 j = 9 j = 10
i = 4
j = 1 j = 2 j = 3 j = 4 j = 5 j = 6 j = 7 j = 8 j = 9 j = 10
i = 5
j = 1 j = 2 j = 3 j = 4 j = 5 j = 6 j = 7 j = 8 j = 9 j = 10
'''

'''
Not:
Python'da bulunan print fonksiyonunda end parametresine varsayılan olarak \n
atanmıştır. Yani alt satıra geç demektir. Eğer biz end = " " eklersek bir boşluk bırakır.
Ya da end = "\t" eklersek bir tab boşluk bırakır.
'''


for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print("")


# Yukarıdaki iç içe for döngüsü aşağıda görülen çıktıyı bize verir.
'''
*
* *
* * *
* * * *
* * * * *
'''


# Aşağıdaki for döngüsü 5 den başlar ve 0'a kadar 1'er azalarak yazdırır.
for i in range(5,0,-1): 
    print(i)




for i in range(10,0,-1):
    for j in range(i):
        print("*",end = " ")
    print("")

# Yukarıdaki iç içe for döngüsü aşağıda görülen çıktıyı bize verir.
'''
* * * * * * * * * * 
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1,11):
    print(f"{1} * {i} = {1 * i}")

# Yukarıdaki for döngüsü aşağıda görülen çıktıyı bize verir. Çarpım tablosunun 1'ler sütunu
'''
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10
'''


for i in range(1,6):
    print(f"{i} * {1} = {i * 1}", end = "    ")

# Yukarıdaki for döngüsü aşağıda görülen çıktıyı bize verir. Çarpım tablosunun 1'ler sütunu
# 1 * 1 = 1    2 * 1 = 2    3 * 1 = 3    4 * 1 = 4    5 * 1 = 5  


# Aşağıdaki iç içe for döngüsü çarpım tablosunu yazdırır.
for i in range(1,11):
    for j in range(1,11):
        print(f"{j} * {i} = {j * i}", end = "\t")
    print("")



# İç içe listeler

listeler = [[2, 1, 5, 7], ["abc", "xyz", 5, 3.5], [1.4, 2, 0, 7]]

print(type(listeler)) # Listenin tipini yazdırır.
print(listeler)
print(listeler[1]) # listeler değişkeninde bulunan 2. sıradaki elemanı yazdırır. Yani: ["abc", "xyz", 5, 3.5] 
print(listeler[1][1]) #2. listenin 2. elemani


for liste in listeler:
    for eleman in liste:
        print(eleman, end="\t")
    print("")

# Yukarıdaki iç içe for döngüsü listeler değişkeninde bulunan listeleri 
# aşağıdaki gibi alt alta yazdırır
'''
2       1       5       7
abc     xyz     5       3.5
1.4     2       0       7
'''


notlar = [["Matematik","Turkce","Cografya"], [80, 100, 95], [70,65,75], [20,15,45]]

notlar2 = [["Matematik", 80, 100, 95], ["Turkce",70,65,75], ["Cografya",20,15,45]]

notlar3 = [["Ahmet",["Matematik", 80, 100, 95], ["Turkce",70,65,75], ["Cografya",20,15,45]],
           ["Bilge",["Matematik", 80, 100, 95], ["Turkce",70,65,75], ["Cografya",20,15,45]],
           ["Kagan",["Matematik", 80, 100, 95], ["Turkce",70,65,75], ["Cografya",20,15,45]]]




for i in range(1, len(notlar)):
    print(f"{notlar[0][i-1]}: ", end = "\t")
    for j in range(len(notlar[i])):
        print(notlar[i][j], end = " ")
    print("")

# Yukarıdaki iç içe for döngüsü bize aşağıdaki çıktıyı verir.
'''
Matematik:      80 100 95 
Turkce:         70 65 75
Cografya:       20 15 45
'''



# Aşağıdaki fonksiyon kendisine parametre olarak verilen listedeki 
# elemanların ortalamasını bulur ve dönderir
def ortBul(liste):
    toplam = 0
    for item in liste:
        toplam += item
    return toplam / len(liste)


# Aşağıdaki fonksiyon kendisine parametre olarak verilen listedeki 
# maksimum elemanı bulur ve dönderir
def maxBul(liste):
    max = liste[0]
    for item in liste:
        if item > max:
            max = item
    return max




for i in range(1, len(notlar)):
    print(f"{notlar[0][i-1]}: ", end = "\t")
    print(ortBul(notlar[i]))

# Yukarıdaki for döngüsü ortBul fonksiyonunu çağırır ve 
# derslerin not ortalamalarını aşağıdaki gibi yazdırır
'''
Matematik:      91.66666666666667
Turkce:         70.0
Cografya:       26.666666666666668
'''



for i in range(1, len(notlar)):
    print(f"{notlar[0][i-1]}: ", end = "\t")
    print(maxBul(notlar[i]))

# Yukarıdaki for döngüsü maxBul fonksiyonunu çağırır ve 
# derslerin en yüksek notlarını aşağıdaki gibi yazdırır
'''
Matematik:      100
Turkce:         75
Cografya:       45
'''
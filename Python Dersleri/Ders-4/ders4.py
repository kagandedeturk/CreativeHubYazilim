
'''
gun = int(input("Haftanin gununu giriniz: "))
saat = int(input("Saati giriniz:\n"))
yas = int(input("Yasinizi giriniz: "))

if gun == 6 or gun == 7:
    print("Hafta sonu sokaga cikma yasagi bulunmaktadir. Sokaga cikamazsiniz")
elif gun >= 1 and gun <= 5:
    if yas >= 65:
        if saat >= 10 and saat <= 13:
            print("Saat 13:00'a kadar sokaga cikabilirsiniz")
        else:
            print("Sokaga cikamazsiniz")
    elif yas < 20:
        if saat >= 13 and saat <= 16:
            print("Saat 16:00'a kadar sokaga cikabilirsiniz")
        else:
            print("Sokaga cikamazsiniz")
    else:
        if saat >= 5 and saat <= 21:
            print("Saat 21:00'a kadar sokaga cikabilirsiniz")
        else:
            print("Sokaga cikamazsiniz")
else:
    print("1 ve 7 arasinda gecerli bir gun giriniz")
'''

'''
alt = int(input("alt degerini giriniz: "))
ust = int(input("Ust degerini giriniz: "))

sonuc = 1
for i in range(ust):
    sonuc = sonuc * alt
print(f"{alt}**{ust} = {sonuc}")
'''

'''
alt = int(input("alt degerini giriniz: "))
ust = int(input("Ust degerini giriniz: "))
sonuc = 1
i = 0
while i < ust:
    sonuc *= alt
    i += 1
print(f"{alt}**{ust} = {sonuc}")
'''


'''
ikili = input("Ikili sistemde ifade edilen sayiyi giriniz: ")
metin_uzunluk = len(ikili)

sonuc = 0

for i in range(metin_uzunluk):
    sonuc += int(ikili[metin_uzunluk-1-i]) * (2**i)

print(f"{ikili}--->{sonuc}")
'''

a = 3
b = "Merhaba"


#List
'''
sehirler = ["Kayseri","Konya","Ankara","Istanbul"]

sehir1 = "Kayseri"
sehir2 = "Konya"

print(sehirler)

sayilar = [1, 3, 11, 2, 2.3, 3.75]

print(sayilar)

karisik = ["ali", 2, 3.75]

print(karisik)

# Listenin elemanlarina index ile erisme

print(sayilar[0])
print(sayilar[1])
print(sayilar[2])
'''

#print(len(sayilar))


sayilar = [1, 3, 11, 2, 2.3, 3.75]
'''
print(sayilar[len(sayilar)-1]) #Listenin son elemanina erisim

print(sayilar[-1])  #Listenin son elemanina erisim

print(sayilar[-2]) #Listenin sondan bir onceki elemanina erisim

a = "Ahm"

liste = ["A","h","m"]

b = liste[0] + liste[1] + liste[2]

print(a)
print(b)


sayilar.append(21) # sayilar listesinin sonuna 21 sayısını ekler


sayilar.remove(2) # sayilar listesinden 2 sayısını çıkartır

sayilar.sort() # sayilar listesini sıralar
sayilar.reverse() # sayilar listesini tersine çevirir



print(sayilar.pop(3)) # sayilar listesinin 4. sırasındaki elemanı siler
# pop(3) ifadesinde 3 sayısı index numarasıdır. 
# Python'da index 0 dan başladığı için index 3 olduğunda 4. sırayı ifade eder
print(sayilar)
'''



# sayilar listesinde minimum elemanı bulan ve yazdıran program
sayilar = [15, 3, 11, 2, 2.3, 3.75]
min = sayilar[0]
for index in range(len(sayilar)):
    if sayilar[index] < min:
        min = sayilar[index]
print(f"Minimum Sayi = {min}")


# sayilar listesindeki sayıları toplayan ve yazdıran program
toplam = 0
for index in range(len(sayilar)):
    toplam = toplam + sayilar[index]
print(f"Toplam = {toplam}")


# sayilar listesindeki sayıların ortalamasını bulan ve yazdıran program
toplam = 0
for index in range(len(sayilar)):
    toplam = toplam + sayilar[index]

print(f"Ort = {toplam/len(sayilar)}")


# sayilar listesinde aranan bir sayının hangi index'te olduğu bulan ve yazdıran program
# Not: sayıyı bulamazsa aranan index değerini -1 yapar ve herhangi bir şey yazdırmaz
sayilar = [15, 3, 11, 2, 2.3, 3.75, 2, 5, 2, 7, 2, 1]
aranan = 2
aranan_index = -1
for index in range(len(sayilar)):
    if sayilar[index] == aranan:
        aranan_index = index
        break
if aranan_index != -1
    print(f"Aranan index = {aranan_index}, aranan eleman = {sayilar[aranan_index]}")


# sayilar listesinde aranan 2 sayısının kaç adet bulunduğunu hesaplayıp yazdıran program
sayilar = [15, 3, 11, 2, 2.3, 3.75, 2, 5, 2, 7, 2, 1]
aranan = 2
adet = 0
for index in range(len(sayilar)):
    if sayilar[index] == aranan:
        adet += 1
print(f"{aranan} sayisi bu listede {adet} adet var")


# Fonksiyon kullanmadan
'''
(2! + 5! + 7!)/(2**3 + 3**5)

fak2 = 1
for i in range(1, 3):
    fak2 = fak2 * i


fak5 = 1
for i in range(1, 5):
    fak5 = fak5 * i

fak7 = 1
for i in range(1, 7):
    fak7 = fak7 * i


(fak2 + fak5 + fak7) / ...
'''


#Fonksiyonlar

def fonk_ismi():
    ...

def fonk_ismi(parametre1, parametre2,...,parametreN):
    ...


# Deger döndermeyen fonksiyonlar
def yazdir():
    print("Python Dersine hosgeldiniz")


yazdir() # Fonksiyonun çağrılması
yazdir() # Fonksiyonun çağrılması
yazdir() # Fonksiyonun çağrılması



def yaz(x):
    print(x)


yaz("Python Dersi") # yaz fonksiyonunun çağrılması
yaz(3.75)
yaz(5)
yaz("Merhaba Dunya")


# Deger dönderen fonksiyonlar
def topla(a, b):
    return a + b

def carpma(a,b):
    return a * b


print(topla(3,5)) # topla fonksiyonunun çağrılması
print(topla(7,11))
print(topla(123,235))

print(carpma(5,11)) # carpma fonksiyonunun çağrılması



# sayilar listesinde aranan bir sayının 
# kaç adet geçtiğini hesaplayıp yazdıran program 
# kaç adet geçtiğini fonksiyon kullanarak hesaplamaktadır

sayilar = [15, 3, 11, 2, 2.3, 3.75, 2, 5, 2, 7, 2, 1, 3, 1, 5, 3]

def adetBul(eleman,liste):
    adet = 0
    for i in range(len(liste)):
        if liste[i] == eleman:
            adet += 1
    return adet

print(f"2 sayisi listede {adetBul(2,sayilar)} adet var")
print(f"3 sayisi listede {adetBul(3,sayilar)} adet var")
print(f"1 sayisi listede {adetBul(1,sayilar)} adet var")
print(f"5 sayisi listede {adetBul(5,sayilar)} adet var")


'''
Yukarıda sayilar listesi içerisinde sırasıyla 2, 3, 1 ve 5 sayılarının 
kaç adet geçtiğini yazdırdık. Fonksiyon kullanmasaydık her bir aranan sayı için
for döngüsü yazmamız gerekecekti. 
Fonksiyon bize hem büyük bir kolaylık sağladı hem de işimizi oldukça kolaylaştırdı.
'''



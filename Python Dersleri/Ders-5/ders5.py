

# Değer döndermeyen parametresiz fonksiyon yazımı:
def topla():
    print(f"3 + 5 = {3+5}")

topla() # Fonksiyonu çağırma


# Değer döndermeyen parametreli fonksiyon yazımı:
def topla2(x,y):
    print(f"{x} + {y} = {x+y}")

topla2(12,25) # Fonksiyonu çağırma


# Değer dönderen parametreli fonksiyon yazımı:
def parametreli_topla(x, y):
    return x + y

# Fonksiyonu çağırma ve fonksiyondan dönen değeri değişkene atama
toplam = parametreli_topla(7, 11) 
print(f"toplam = {toplam}")

# Farklı parametre değerleriyle parametreli_topla fonksiyonunu çağırma
# ve fonksiyondan dönen sonucu yazdırma
print(f"toplam2 = {parametreli_topla(2, 5)}") 
print(f"toplam3 = {parametreli_topla(3, 6)}")
print(f"toplam4 = {parametreli_topla(4, 7)}")


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


# sayilar listesindeki elemanları sırayla yazdırma
for i in range(len(sayilar)): 
    print(sayilar[i])

# bir üstteki for döngüsünde olduğu gibi sayilar listesindeki elemanları sırayla yazdırır 
# fakat daha kolay bir şekilde
for eleman in sayilar:
    print(eleman)



# Aşağıdaki fonksiyon string bir değişkende aranan karakterin toplamda kaç adet geçtiğini dönderir.
def adetBul(isim,harf):
    adet = 0
    for i in range(len(isim)):
        if isim[i] == harf:
            adet += 1
    return adet



'''
Soru:
İki farklı isimde sırasıyla true ve love stringlerindeki karakterlerin toplam görünme sayılarını hesaplayıp
Yüzde işaretiyle birlikte yan yana yazdıran program.
İki isim arasında gerçek sevgi olup olmadığını hesaplama yöntemi :))
ör: Ahmet Salur ve Zeynep Deneme isimlerinde 
true stringindeki t harfi 1 adet, r harfi 1 adet, u harfi 1 adet ve e harfi 6 adet geçmektedir.
Bu iki isimde true stringindeki harfler toplam 9 adet geçmektedir.
Bu iki isimde love stringindeki l harfi 1 adet, o harfi 0 adet, v harfi 0 adet ve e harfi 6 adet geçmektedir.
Yani bu iki isimde love stringindeki harfler toplam 7 adet geçmektedir.
Sonuç: %97 true love 
'''
isim1 = "Ahmet Salur"
isim2 = "Zeynep Deneme"
isimler = isim1 + isim2 # İki ismi 
isimler = isimler.lower() # Stringdeki büyük harfleri küçüğe çevirir.

# Aşağıdaki fonksiyon kendi içerisinde adetBul fonksiyonunu çağırır 
# Bu fonksiyon string bir değişkende başka bir string değişkende herbir harfin geçme sayılarının toplamını dönderir
# ör: dedeturk stringinde true stringinde yer alan harflerin gözükme sayılarının toplamı
# dedeturk stringinde t harfi 1 adet var
# dedeturk stringinde r harfi 1 adet var
# dedeturk stringinde u harfi 1 adet var
# dedeturk stringinde e harfi 2 adet var
# 1 + 1 + 1 + 2 = 5
# Yani bu fonksiyona sırasıyla dedeturk ve true parametrelerini gönderirsek bize 5 değerini dönderir
def toplamKarakterAdedi(isim,aranan):
    toplam_adet = 0
    for i in range(len(aranan)):
        toplam_adet += adetBul(isim,aranan[i])
    return toplam_adet


true_sayisi = toplamKarakterAdedi(isimler,"true")
love_sayisi = toplamKarakterAdedi(isimler,"love")
print(f"%{true_sayisi}{love_sayisi}")


'''
true_sayisi = 0
for i in range(len("true")):
    true_sayisi += adetBul(isimler,"true"[i])

love_sayisi = 0
for i in range(len("love")):
    love_sayisi += adetBul(isimler,"love"[i])

for i in range(len("true")):
    for j in range(len(isimler)):
        if isimler[j] == "true"[i]:
            true_sayisi += 1
'''


# Klavyeden alınan bir sayının asal sayı olup olmadığını yazdıran program
sayi = int(input("sayiyi giriniz: "))

asal_mi = True
if sayi < 2:
    asal_mi = False
else:
    for i in range(2,sayi):
        if sayi % i == 0:
            asal_mi = False
            break
if asal_mi:
    print(f"{sayi} sayısı asal sayıdır")
else:
    print(f"{sayi} sayısı asal değildir")


# 1 ile 100 arasındaki asal sayıları yazdıran program
for sayi in range(1,101):
    asal_mi = True
    if sayi < 2:
        asal_mi = False
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                asal_mi = False
                break
    if asal_mi:
        print(sayi)


# Parametre olarak verilen bir sayı asalsa True asal sayı değilse False dönderen fonksiyon
def asal_mi(sayi):
    sonuc = True
    if sayi < 2:
        sonuc = False
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                sonuc = False
                break
    return sonuc


# 1 ile 1000 arasındaki asal sayıları asal_mi fonksiyonunu kullanarak bulan ve yazdıran program
for sayi in range(1,1001):
    if asal_mi(sayi):
        print(sayi)



# RANDOM

import random   #random modülünü programımıza ekleme

print(random.random()) # 0 ile 1 arasında rastgele üretilen float sayıyı yazdırır. Random float:  0.0 <= x < 1.0   

print(random.randrange(1,10)) # 1 ile 9 arasında rastgele bir tam sayı üretir

print(random.randint(1,10)) # 1 ile 10 arasında rastgele bir tam sayı üretir


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
secim = int(input("Tasi secmek icin 0, kagidi secmek icin 1 ve makasi secmek icin 2 giriniz: "))

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




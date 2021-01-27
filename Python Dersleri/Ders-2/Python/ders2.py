# Degiskenler

x = 5                     # int degisken
y = 3.87                  # float degisken
kurs_adi = "Python kursu" # string degisken

# Degiskenin Tipini Ogrenme

'''
print(f"Degiskenin tipi = {type(x)}")

print(type(y))
print(type(kurs_adi))
'''

# Tip Donusumleri

str_tamsayi = "5"
str_floatsayi = "7.5"
tamsayi = int(str_tamsayi)
floatsayi = float(str_floatsayi)

'''
print(type(str_tamsayi))
print(type(str_floatsayi))
print(type(tamsayi))
print(type(floatsayi))


print(str_tamsayi + str_floatsayi)  # 57.5
print(tamsayi + floatsayi) # 12.5


print(str(3.4) + str(5))
print(3.4 + 5)

print(int("a"))
'''

# Aritmatik Operatorler

sayi1 = 3
sayi2 = 2

toplam = sayi1 + sayi2 # 5
cikarma = sayi1 - sayi2 # 1
carpma = sayi1 * sayi2 # 6
bolme = sayi1 / sayi2  # 1.5
us_alma = sayi1 ** sayi2 # 9
kalan = sayi1 % sayi2 # 1
taban_bolme = sayi1 // sayi2 # 1
saga_bit_kaydirma = 4 >> 1
sola_bit_kaydirma = 4 << 1
'''
print(toplam)
print(cikarma)
print(carpma)
print(bolme)
print(us_alma)
print(kalan)
print(taban_bolme)

print(saga_bit_kaydirma)
print(sola_bit_kaydirma)

print(f"{sayi1} + {sayi2} = {toplam}")

# print(str(sayi1) + " + " + str(sayi2) + " = " + str(toplam))

print(f"{sayi1} * {sayi2} = {carpma}")
'''

# islem onceligi

# Parantez
# us alma
# carpma ve bolme
# mod ve taban_bolme
# toplama ve cikarma
# soldan saga

'''
print(3 * 3 + 3 / 3 - 3) # 7.0
#print(9 + 3 / 3 - 3)
#print(9 + 1.0 - 3)

print(2 * 5 % 3)


print(2 * 3 ** 2) # 18
print((2 * 3) ** 2)
'''


'''
sayi1 = int(input("1. sayiyi giriniz: "))
sayi2 = int(input("2. sayiyi giriniz: "))

toplam = sayi1 + sayi2 

print("Iki sayinin toplami = " + str(toplam))

print(f"{sayi1} + {sayi2} = {toplam}")
'''

# Soru 2
'''
boy = float(input("Boy bilginizi metre cinsinden giriniz: "))
kilo = float(input("Kilo bilginizi kg cinsinden giriniz: "))

vki = kilo / (boy * boy)

print(f"Vucut kitle endeksiniz = {vki}")
'''

# Soru 3
'''
yas = int(input("Yasiniz giriniz: "))

yil = 90 - yas
ay = (90 - yas) * 12
hafta = (90-yas) * 52
gun = (90-yas) * 365
print(f"{gun} gununuz, {hafta} haftaniz, {ay} ayiniz, {yil} yiliniz kaldi")
'''

# Soru 4

'''
hesap = float(input("Hesap ne kadar tuttu: "))
bahsis = float(input("Yuzde cinsinden bahsis miktarini giriniz: "))
kisi_sayisi = int(input("Kac kisi odeyeceksiniz: "))

kisi_basi_ucret = (hesap + (hesap * bahsis / 100)) / kisi_sayisi

print(f"Kisi basi odenecek ucret = {kisi_basi_ucret} TL")
'''

'''
# Us alma islemi yapan program
alt = int(input("alt degerini giriniz: "))
ust = int(input("ust degerini giriniz: "))
sonuc = alt ** ust
print(f"{alt} uzeri {ust} = {sonuc}")
'''

# Kosul Ifadeleri

'''
n = 5
m = -3


sonuc = n > 0
sonuc2 = m > 0


print(sonuc)        # True
print(sonuc2)       # False
print(type(sonuc))  # <class 'bool'>

# buyuk mu '>'
# >, <, ==, <=, >=, !=


print(3 != 5) #True
print(3 != 3) #False

print(3 == 3) #True
print(5 == 7) #False
 
print(11 <= 11) #True


n = -5
if n > 0:
    print(f"{n} sayisi pozitif bir sayidir")
else:
    print(f"{n} sayisi negatif bir sayidir")

'''

sayi = float(input("Klavyeden bir sayi giriniz: "))


if sayi > 0:
    print(f"{sayi} sayisi pozitif bir sayidir")
elif sayi == 0:
    print(f"{sayi} sayisi isaretsiz bir sayidir")
else:
    print(f"{sayi} sayisi negatif bir sayidir")



if sayi % 2 == 0:
    print(f"{sayi} sayisi cift bir sayidir")
elif sayi % 2 == 1:
    print(f"{sayi} sayisi tek bir sayidir")


if sayi % 2 == 0:
    print(f"{sayi} sayisi cift bir sayidir")
else:
    print(f"{sayi} sayisi tek bir sayidir")


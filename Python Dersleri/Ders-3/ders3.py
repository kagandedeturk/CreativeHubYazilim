# ic ice kosul ifadeleri

'''
boy = int(input("boyunuz kac cm? "))

if boy > 120:
    print("Gondola binebilirsiniz")
    yas = int(input("yasinizi giriniz: "))
    if yas < 12:
        print("10 TL")
    elif yas < 18
        print("20 TL")
    else:
        print("40 TL")
else:
    print("Gondola binemezsiniz")

'''
# Mantiksal operatorler

# and, or, not

'''
print(True and False)
print(True or False)
print(True & False) # and operatoru
print(True | False) # or operatoru
'''

#print(False and True or True)

'''
print(5 > 3 and 7 > 9)
print(1 < 3 and 5 > 2)
'''

'''
print(not True)

print(not(True and False))

print(not True or not False)



if sart1:
    print("sart1")
elif sart2:
    print("sart2")
elif sart3:
    print("sart3")
else:
    print("diger")


if sart1:
    print("sart1")
if sart2:
    print("sart2")
if sart3:
    print("sart3")
if sart4:
    print("diger")
'''

# vki = kilo(kg) / (boy(m) * boy(m))

# vki < 18.5 zayif
# vki < 25 normal
# vki < 30 kilolu
# vki < 35 obez
# vki >= 35 klinik yaka

'''
boy = float(input("boyunuzu cm cinsinden giriniz: ")) / 100
kilo = float(input("kilonuzu giriniz: "))

vki = kilo / (boy * boy)


if vki < 18.5:
    print(f"vki = {vki}, zayif")
elif vki < 25:
    print(f"vki = {vki}, normal")
elif vki < 30:
    print(f"vki = {vki}, kilolu")
elif vki < 35:
    print(f"vki = {vki}, obez")
else:
    print(f"vki = {vki}, klinik vaka")



if vki >= 30 and vki < 35:
    print(f"vki = {vki}, obez")
if vki >= 25 and vki < 30:
    print(f"vki = {vki}, kilolu")
if vki >= 18.5 and vki < 25:
    print(f"vki = {vki}, normal")
if vki < 18.5:
    print(f"vki = {vki}, zayif")
if vki >= 35:
    print(f"vki = {vki}, klinik vaka")
'''


'''
Haftanin gunu sayi olarak giriniz. Pazartesi ise 1, Sali ise 2, Pazar ise 7 seklinde
yasinizi giriniz
saati giriniz
20 ile 65 yas arasinda
'''

# Donguler
'''
for sayi in range(5):
    print(sayi)
'''

'''
for i in range(1,11):
    print(i)

#print(i)

'''

# for degisken_ismi in range(baslangic_degeri, bitis_degeri, artirma_degeri):

'''
for i in range(1,11,4):
    print(i)
'''

'''
toplam = 0
for sayi in range(1,5):
    toplam = toplam + sayi  # toplam += sayi

print(f"toplam={toplam}")


for sayi in range(1,101):
    if sayi % 7 == 0:
        print(sayi)
'''

'''
for sayi in range(1,101):
    if sayi % 2 == 1:
        print(sayi)
'''

# 5! = 1 * 2 * 3 * 4 * 5 = 120

'''
sayi = int(input("Sayiyi giriniz: "))
fak = 1
for i in range(1, sayi+1):
    fak = fak * i
print(f"{i}! = {fak}")
'''

# klavyeden alinan alt ve ust degerlerine gore alt uzeri 
# ust degerini for dongusu kullanarak hesaplayan program

'''
sayi = 1
while sayi <= 5:
    print(sayi)
    sayi = sayi + 1
'''
'''
toplam = 0
sayi = 1
while sayi <= 5:
    toplam += sayi
    sayi = sayi + 1

print(toplam)
'''
'''
bas_deg = int(input("baslangic degerini giriniz: "))
bit_deg = int(input("bitis degerini giriniz: "))
toplam = 0
while bas_deg <= bit_deg:
    toplam += bas_deg
    bas_deg = bas_deg + 1

print(toplam)
'''

'''
sonuc = 1
sayi = int(input("sayiyi giriniz: "))
i = 1
while i <= sayi:
    sonuc *= i
    i += 1
print(f"{sayi}! = {sonuc}")
'''
'''
not_sonuc = float(input("Notunuzu giriniz: "))

while not(not_sonuc >= 0 and not_sonuc <= 100):
    print(f"Lutfen 0 ile 100 arasinda bir deger giriniz. Siz {not_sonuc} girdiniz!")
    not_sonuc = int(input("Notunuzu giriniz: "))

print(f"Notunuz : {not_sonuc}")
'''

'''
not_sonuc = float(input("Notunuzu giriniz: "))

# (a and b)' = a' or b'

while not_sonuc < 0 or not_sonuc > 100:
    print(f"Lutfen 0 ile 100 arasinda bir deger giriniz. Siz {not_sonuc} girdiniz!")
    not_sonuc = int(input("Notunuzu giriniz: "))

print(f"Notunuz : {not_sonuc}")
'''

'''
sayi = int(input("Ikili sisteme donusturulecek sayiyi giriniz: "))
ikili_sistem = ""

while sayi > 0:
    ikili_sistem = str(sayi % 2) + ikili_sistem
    sayi = sayi // 2

print(ikili_sistem)
'''

print("1000"[3])

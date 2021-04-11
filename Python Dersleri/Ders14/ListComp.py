


'''
l = [1, 2, 3, 4]

# l2 = [2, 3, 4, 5]

# l2 = []
# for eleman in l:
#     l2.append(eleman + 1)

# print(l2)

#List Comprehension
# yeni_liste = [yeni deger for item in liste]
l2 = [eleman + 1 for eleman in l]
print(l2)


l3 = [i ** 2 for i in l]
print(l3)
'''

'''
liste = [3, 1, 0, 5, 6, 11, 22, 8, 9 ,7]
# cift_sayilar = []
# for item in liste:
#     if item % 2 == 0:
#         cift_sayilar.append(item)

# print(cift_sayilar)


#List Comprehension
# yeni_liste = [yeni_deger for i in liste if sart]
cift_sayilar = [i for i in liste if i % 2 == 0]
print(cift_sayilar)
'''

'''
isim = "Bilge"
#['B','i','l','g','e']
harfler = []
for harf in isim:
    harfler.append(harf)

print(harfler)    
'''

l1 = [3, 1, 5, 2, 9, 8, 7, 15]
l2 = [11, 1, 6, 2, 5, 8, 33, 22]

# print(333 in l1)

# ortak = []
# for i in l1:
#     if i in l2:
#         ortak.append(i)
# print(ortak)

# yeni_liste = [yeni_deger for i in liste if sart]

'''
ortak = [sayi for sayi in l1 if sayi in l2]
print(ortak)


l1_fark_l2 = [sayi for sayi in l1 if sayi not in l2]
print(l1_fark_l2)

l2_fark_l1 = [sayi for sayi in l2 if sayi not in l1]
print(l2_fark_l1)



birlesim = l1_fark_l2 + l2_fark_l1 + ortak
print(birlesim)
'''

'''
birlesim = [sayi for sayi in l1 if sayi in l2]
birlesim += [sayi for sayi in l1 if sayi not in l2]
birlesim += [sayi for sayi in l2 if sayi not in l1]
'''




# sozluk = {
#     "a" : 1,
#     "b" : 2,
#     1 : 5
# }

# print(sozluk)

#Dictionary Comprehension
## yeni_sozluk = {yeni_anahtar:yeni_deger for (anahtar,deger) in sozluk.items()}

# yeni_sozluk = {key: value + 1 for (key,value) in sozluk.items()}
# print(yeni_sozluk)


import random as rnd
liste = ['Kagan','Mehmet',"Beyhan","Ahmet",'Melike']

isim_zar = {isim: rnd.randint(1,7) for isim in liste}
print(isim_zar)
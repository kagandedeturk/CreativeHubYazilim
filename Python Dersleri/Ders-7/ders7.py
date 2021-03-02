# Dictionary (Sözlük) Veri Yapısı

'''
Pythonda sözlük (dictionary) veri yapısında veriler 
Anahtar-Değer (Key-Value) ikilisi olarak tutulurlar
'''
#sozluk = {} # Bos Sozluk Tanimlama 


sozluk = {
    "make": ["yapmak","elde etmek","yapi"],
    "initialize": ["ilk kullanima hazirlamak","baslatmak"],
    "function": "fonksiyon",
    "do": "yapmak",
    123 : "sayi"
}

print(sozluk) 
print(sozluk["make"]) # Sözlükteki "make" anahtarının değerini yazdırır

print(sozluk["initialize"]) # Sözlükteki "initialize" anahtarının değerini yazdırır

#print(sozluk["funtion"])

sozluk["start"] = "baslatmak"

print(sozluk) 

personeller = {
    25199112345 : "Bilge Kagan Dedeturk",
    23233242123 : "Ahmet Yagmur"
}

print(personeller)

liste = []
personeller = {}

print(personeller)


for kelime in sozluk:
    print(f"{kelime}: {sozluk[kelime]}")

# Yukarıdaki for döngüsü ile aşağıdaki for döngüsü aynı çalışır
for k,v in sozluk.items():
    print(f"{k}: {v}")



yolculuk_gecmisi = {
    "Turkiye": ["Ankara","Antalya","Istanbul"],
    "Fransa": ["Paris","Lille"],
    "Almanya":["Berlin","Hamburg"]
}

for k,v in yolculuk_gecmisi.items():
    print(f"{k}:", end = " ")
    for sehir in v:
        print(sehir,end=", ")
    print("")




yolculuk_gecmisi_2 = {
    "Turkiye": {"Ziyaret Sehirleri":["Ankara","Antalya","Istanbul"],"Ziyaret Sayisi":12},
    "Fransa": {"Ziyaret Sehirleri":["Paris","Lille"],"Ziyaret Sayisi":5},
    "Almanya":{"Ziyaret Sehirleri":["Berlin","Hamburg"],"Ziyaret Sayisi":7}
}

print(yolculuk_gecmisi_2)




yolculuk_gecmisi_3 = [
    {
        "Ulke":"Turkiye",
        "Ziyaretler": 12,
        "Sehirler": ["Ankara","Antalya","Istanbul"]
    },
    {
        "Ulke":"Almanya",
        "Ziyaretler": 7,
        "Sehirler": ["Berlin","Hamburg"]
    },
    {
        "Ulke":"Fransa",
        "Ziyaretler": 5,
        "Sehirler": ["Paris","Lille"]
    }
]


for eleman in yolculuk_gecmisi_3:
    ulke = eleman["Ulke"]
    print(f"{ulke}: ", end="")
    for sehir in eleman["Sehirler"]:
        print(sehir, end=", ")
    print("")



def ulkeEkle(ulke, ziyaretSayisi, sehirler):
    ulke_sozluk = {}
    ulke_sozluk["Ulke"] = ulke
    ulke_sozluk["Ziyaretler"] = ziyaretSayisi
    ulke_sozluk["Sehirler"] = sehirler
    yolculuk_gecmisi_3.append(ulke_sozluk)


ulkeEkle("Rusya",2,["Moskova","Petersburg"])



print("---------------------------------------")

for eleman in yolculuk_gecmisi_3:
    ulke = eleman["Ulke"]
    print(f"{ulke}: ", end="")
    for sehir in eleman["Sehirler"]:
        print(sehir,end=", ")
    print("")


yolculuk_gecmisi_4 = {
    "Turkiye":{
        "Ziyaretler": 12,
        "Sehirler": ["Ankara","Antalya","Istanbul"]
    },
    "Almanya":{
        "Ziyaretler": 7,
        "Sehirler": ["Berlin","Hamburg"]
    },
}

#CLASS (SINIF)

#import random

#print(random.randint(1,10))

#import ders4

#print(ders4.sehirler)

#print(ders4.topla(3,23))



from sekiller import Dikdortgen

dik1 = Dikdortgen() # bir classtan nesne yaratma

print(dik1)

dik2 = Dikdortgen()

print(dik2)

#dik2.uzunKenar = 7


dik1.setKisaKenar(5)
dik1.setUzunKenar(12)

dik2.setKisaKenar(7)
dik2.setUzunKenar(24)

print(f"dik1 Uzun Kenar = {dik1.uzunKenar}")
print(f"dik2 Uzun Kenar = {dik2.uzunKenar}")


print(f"dik1 cevre = {dik1.cevre()}")
print(f"dik2 cevre = {dik2.cevre()}")


print(f"dik1 alan = {dik1.alan()}")
print(f"dik2 alan = {dik2.alan()}")


dik1 = Dikdortgen(uzunKenar=24,kisaKenar=7)
print(f"dik1 Uzun Kenar = {dik1.uzunKenar}")
print(f"dik1 cevre = {dik1.cevre()}")
print(f"dik1 alan = {dik1.alan()}")


from sekiller import Daire

d1 = Daire(3)

print(f"d1 dairesinin cevresi = {d1.cevre()}")
print(f"d1 dairesinin alani = {d1.alan()}")
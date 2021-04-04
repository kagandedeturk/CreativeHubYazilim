

# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     print(dosya.read())



# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     print(dosya.readlines())


# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     satirlar = dosya.readlines()
#     for satir in satirlar:
#         #print(satir,end="")
#         print(satir.strip())


# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     satirlar = dosya.readlines()
#     for satir in satirlar[1:]:
#         #print(satir,end="")
#         print(satir.strip())

# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     satirlar = dosya.readlines()
#     for satir in satirlar[1:]:
#         veri = satir.split(",")
#         print(veri)


# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     satirlar = dosya.readlines()
#     for satir in satirlar[1:]:
#         veri = satir.split(",")
#         sicaklik = veri[1]
#         print(sicaklik)


# import csv
# with open("./Ders-13/Pandas/havadurumu.csv") as dosya:
#     veri = csv.reader(dosya)
#     #print(veri)
#     for satir in veri:
#         if satir[1] != 'temp':
#             print(satir[1])



import pandas

veri = pandas.read_csv("./Ders-13/Pandas/havadurumu.csv")
#print(veri)

# print(veri[:])



# print(veri.head())

sicaklik = veri["temp"]
gunler = veri["day"]

print(sicaklik)

print(sicaklik[3:5])
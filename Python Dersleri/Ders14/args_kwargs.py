
'''
def topla(a,b,c,d,e):
    return a + b + c + d + e 

print(topla(1,2,3,4,5))
#print(topla(1,2)) # Hata verir
'''

'''
def topla(a = 0, b = 0, c = 0, d = 0, e = 0):
    return a + b + c + d + e 


print(topla())
print(topla(1,2))
# print(topla(1,2,3,4,5,6)) #Hata verir
'''

'''
def yazdir(a = 0, b = 0, c = 0, d = 0, e = 0):
    print(a, b, c, d, e)


yazdir(1, 3)
yazdir(0, 0, 0, 1, 3)
yazdir(e = 3, d = 1)
yazdir(d = 1, e = 3)
yazdir(b = 2, e = 5)
'''

'''
def topla(*args):
    print(type(args))


def topla2(*args):
    print(args)

topla(1,3,5,7,8)
topla2(1,3,5,7,8)
'''

'''
def topla(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla((1,5,7)))
'''


# *args: pozisyonel degisken-uzunluklu argumanlar
'''
def topla(*args):
    toplam = 0
    for item in args:
        toplam += item
    return toplam

print(topla(1, 5, 12, 24, 36, 22))
print(topla(1, 5, 12, 24)) #topla(1, 5, 12, 24)
print(topla(1, 5)) #topla(1, 5)
print(topla(1)) # topla(1)
'''

'''
def topla(*a): # *args ifadesinde args degisken ismi onun yerine istedigimiz degisken ismini verebiliriz. * ifadesini basina koymak sartiyla
    toplam = 0
    for item in a:
        toplam += item
    return toplam

print(topla(1, 5, 12, 24, 36, 22))
print(topla(1, 5, 12, 24)) #topla(1, 5, 12, 24)
print(topla(1, 5)) #topla(1, 5)
print(topla(1)) # topla(1)
'''


# **kwargs : KeyWord arguments, Keyworded variable-length arguments

'''
def hesapla(n, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for (anahtar,deger) in kwargs.items():
    #     print(f"{anahtar} : {deger}")

    n += kwargs["topla"]
    n *= kwargs["carp"]
    n /= kwargs["bol"]
    print(f"sonuc = {n}")


hesapla(2, topla = 5, carp = 3, bol = 2)
'''


"""
sozluk = {
    'topla': 5, 
    'carp': 3
}

print(sozluk["topla"])
"""


# class Araba:
#     def __init__(self, **ad):
#         self.marka = ad['marka']
#         self.model = ad['model']
#         self.renk = ad['renk']
#         self.koltuk = ad['koltuk']

    
# arabam = Araba(marka="Audi", model="A3", renk="siyah", koltuk = 5)
# print(arabam.marka, arabam.model)

'''
class Araba:
    def __init__(self, **ad):
        self.marka = ad.get("marka")
        self.model = ad.get('model')
        self.renk = ad.get('renk')
        self.koltuk = ad.get("koltuk")

arabam = Araba(marka="Audi", model="A3")
print(arabam.marka, arabam.model)
print(arabam.renk)
'''

def bar(adet, yumurta, tost = "evet lutfen", pismis = 0):
    print(adet, yumurta, tost, pismis)

# bar(1,2)


# bar(tost = "hayir", adet = 4, yumurta = 2)


def test(a, *arg, **kw):
    print(a, arg, kw)

test(2, 1, 5, 3, 0, x = 5, y = 10)
test(2, 1, 5, 3, 0, x = 5, y = 10, z = 22, l = [1,3,5])




def faktoriyel(n):
    sonuc = 1
    for i in range(1, n+1):
        sonuc = sonuc * i
    return sonuc

def usHesapla(alt, ust):
    sonuc = 1
    for i in range(ust):
        sonuc *= alt
    return sonuc

def karekok(sayi):
    return sayi ** 0.5

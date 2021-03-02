
from menu import Menu,MenuItem
from para_makinesi import ParaMakinesi

m1 = Menu()

print(m1.get_icecekler())

icecek = m1.icecegi_bul("cappuccino")

print(f"icecek ismi = {icecek.isim}\nmaliyet = {icecek.maliyet}\nicerik = {icecek.icerikler}")


pm = ParaMakinesi()


if pm.odeme_yap(icecek.maliyet):
    pm.rapor()
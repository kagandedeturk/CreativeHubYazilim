
class KahveYapma:
    """Kahveyi yapan makineyi modeller"""

    def __init__(self):
        self.kaynaklar = {
            "su": 300,
            "süt": 200,
            "kahve":100
        }

    def rapor(self):
        """Tum kaynaklari gosteren bir rapor yazdirir."""
        print(f"Su: {self.kaynaklar['su']}ml")
        print(f"Süt: {self.kaynaklar['sut']}ml")
        print(f"Kahve: {self.kaynaklar['kahve']}g")


    def kaynak_yeterli_mi(self, icecek):
        """Siparis yapilabilirse True donderir, makinenin icindekiler yetersizse False donderir"""
        yapilabilir_mi = True
        for item in icecek.icerikler:
            if icecek.icerikler[item] > self.kaynaklar[item]:
                print("İçeceği yapmak için makinede yeterli {item} yok")
                return False
        return yapilabilir_mi

    def kahve_yap(self, siparis):
        """Kaynaklardan yapilan icecegin icerik miktarlarini cikarir."""
        for item in siparis.icerikler:
            self.kaynaklar[item] -= siparis.icerikler[item]
        print(f"{siparis.isim} içeceğinizi alabilirsiniz. Afiyet olsun!")









kahveyap = KahveYapma()

kahveyap.rapor()

print(kahveyap.kaynaklar)
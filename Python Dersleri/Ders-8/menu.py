class MenuItem:
    # Menudeki her bir icecegi modeller
    def __init__(self,isim,su,sut,kahve,maliyet):
        self.isim = isim
        self.maliyet = maliyet
        self.icerikler = {
            "su": su,
            "süt": sut,
            "kahve":kahve
        }

class Menu:
    """Iceceklerle Menuyu modeller."""
    def __init__(self):
        self.menu = [
            MenuItem(isim="latte", su=200, sut=150, kahve=24, maliyet=2.5),
            MenuItem(isim="espresso", su=50, sut=0, kahve=18, maliyet=1.5),
            MenuItem(isim="cappuccino", su=250, sut=50, kahve=24, maliyet=3)
        ]
    
    def get_icecekler(self):
        """Menudeki tum iceceklerin isimlerini donderir"""
        secenekler = ""
        for item in self.menu:
            secenekler += f"{item.isim}/"
        return secenekler

    def icecegi_bul(self, siparis_ismi):
        """Menude siparis verilen icecegin ismini arar. O icecek varsa donderir, yoksa herhangi bir sey dondermez"""
        for item in self.menu:
            if item.isim == siparis_ismi:
                return item
        print("Girdiginiz icecek mevcut degil")
    
    def icecek_ekle(self, isim,su,sut,kahve,maliyet):
        icecek = MenuItem(isim,su,sut,kahve,maliyet)
        self.menu.append(icecek)


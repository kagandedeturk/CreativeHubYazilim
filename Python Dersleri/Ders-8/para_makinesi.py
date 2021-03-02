
class ParaMakinesi:

    para_birimi = "₺"

    para_turleri = {
        "birim":0.10,
        "ceyrek":0.25,
        "yarim":0.50,
        "tl": 1.00
    }

    def __init__(self):
        self.kar = 0
        self.alinan_para = 0

    def rapor(self):
        """Makinedeki mevcut parayi yazdirir"""
        print(f"{self.kar}{self.para_birimi}")
    

    def paralari_isle(self):
        """Verilen paralardan hesaplanan toplami donderir"""
        print("Lutfen parayi yerlestiriniz.")
        for para_turu in self.para_turleri:
            self.alinan_para += int(input(f"Ne kadar {para_turu} yatiracaksiniz?: ")) * self.para_turleri[para_turu]
        return self.alinan_para

    def odeme_yap(self,maliyet):
        """Odeme kabul edilirse True doner. Para yeterli degilse False doner"""
        self.paralari_isle()
        if self.alinan_para >= maliyet:
            para_ustu = round(self.alinan_para - maliyet, 2)
            print(f"{para_ustu}{self.para_birimi} para ustunuzu alabilirsiniz")
            self.kar += maliyet
            self.alinan_para = 0
            return True
        else:
            print("Girdiginiz para yeterli degil. Paraniz iade edildi.")
            self.alinan_para = 0
            return False



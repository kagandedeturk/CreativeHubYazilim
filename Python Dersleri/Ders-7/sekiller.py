
class Dikdortgen: 
    def __init__(self, kisaKenar=5, uzunKenar=12):
        print("Dikdortgen classindan nesne olusturuldu")
        self.kisaKenar = kisaKenar
        self.uzunKenar = uzunKenar

    def cevre(self):
        return 2 * (self.kisaKenar + self.uzunKenar)

    def alan(self):
        return self.kisaKenar * self.uzunKenar

    def setUzunKenar(self,n):
        self.uzunKenar = n

    def setKisaKenar(self,n):
        self.kisaKenar = n


class Kare:
    def __init__(self, kenar = 1):
        print("Kare classindan nesne olusturuldu")
        self.kenar = kenar


    def cevre(self):
        return 4 * self.kenar

    def alan(self):
        return self.kenar ** 2

    def setKenar(self,n):
        self.kenar = n


class Daire:
    def __init__(self, r = 1):
        print("Daire classindan nesne olusturuldu")
        self.yaricap = r
        self.pi = 3.14

    def cevre(self):
        return 2 * self.pi * self.yaricap

    def alan(self):
        return self.pi * self.yaricap * self.yaricap

    def setYaricap(self, r):
        self.yaricap = r
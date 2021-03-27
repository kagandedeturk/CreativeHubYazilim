

class Kopek:
    def __init__(self):
        self.ayak_sayisi = 4
        self.goz_sayisi = 2
        self.durum = "sadik"


    def ses_cikar(self):
        print("Hav hav")



class Pitpul(Kopek):

    def __init__(self):
        super().__init__()
        self.ozellik = "Saldirgan"

    def ses_cikar(self):
        super().ses_cikar()
        print("Haaaaav haaaaaav")


k1 = Kopek()
p1 = Pitpul()

p1.ses_cikar()
print(f"ayak sayisi = {p1.ayak_sayisi}")

print(f"pitbul durum : {p1.durum}")
print(f"kopek durum : {k1.durum}")

print(f"pitbul ozellik : {p1.ozellik}")

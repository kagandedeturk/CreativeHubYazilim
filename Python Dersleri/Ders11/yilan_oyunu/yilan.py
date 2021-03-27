
from turtle import Turtle

class Yilan:

    def __init__(self):
        self.parcalar = []
        self.baslangic_pozisyonlari = [(0,0),(-20,0),(-40,0)]
        self.hareket_mesafesi = 20
        self.YUKARI = 90
        self.ASAGI = 270
        self.SOL = 180
        self.SAG = 0
        self.yilani_olustur()
        self.BAS = self.parcalar[0]



    def yilani_olustur(self):
        for pos in self.baslangic_pozisyonlari:
            self.parca_ekle(pos)


    def parca_ekle(self,pos):
        parca = Turtle("square")
        parca.color("white")
        parca.penup()
        parca.goto(pos)
        self.parcalar.append(parca)


    def hareket_et(self):
        for parca_indeks in range(len(self.parcalar)-1,0,-1):
            yeni_x = self.parcalar[parca_indeks-1].xcor()
            yeni_y = self.parcalar[parca_indeks-1].ycor()
            self.parcalar[parca_indeks].goto(yeni_x,yeni_y)
        self.BAS.forward(self.hareket_mesafesi)



    def yukari(self):
        if self.BAS.heading() != self.ASAGI:
            self.BAS.setheading(self.YUKARI)

    def asagi(self):
        if self.BAS.heading() != self.YUKARI:
            self.BAS.setheading(self.ASAGI)

    def sag(self):
        if self.BAS.heading() != self.SOL:
            self.BAS.setheading(self.SAG)

    def sol(self):
        if self.BAS.heading() != self.SAG:
            self.BAS.setheading(self.SOL)



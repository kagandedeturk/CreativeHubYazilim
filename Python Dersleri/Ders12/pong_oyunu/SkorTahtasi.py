

from turtle import Turtle

class SkorTahtasi(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.sag_skor = 0
        self.sol_skor = 0
        self.guncelle()

    
    def guncelle(self):
        self.clear()
        self.goto(-100,220)
        self.write(self.sol_skor,align="center",font=("Courier",50,"bold"))
        self.goto(100,220)
        self.write(self.sag_skor,align="center",font=("Courier",50,"bold"))


    def sag_skor_arttir(self):
        self.sag_skor += 1
        self.guncelle()

    def sol_skor_arttir(self):
        self.sol_skor += 1
        self.guncelle()
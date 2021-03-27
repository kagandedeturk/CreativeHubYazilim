
from turtle import Turtle

class SkorTahtasi(Turtle):

    def __init__(self):
        super().__init__()
        self.skor = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.guncelle()
        

    def guncelle(self):
        self.write(f"Skor: {self.skor}", align="center",font="Courier")


    def skor_arttir(self):
        self.skor += 1
        self.clear()
        self.guncelle()
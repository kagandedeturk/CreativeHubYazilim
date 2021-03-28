

from turtle import Turtle
import random as rnd

class Top(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.aci = 45
        


    def hareket_et(self):
        self.setheading(self.aci)
        self.forward(10)


    def yansima_yap(self):
        self.aci = (self.aci - 90) % 360

    def basa_don(self):
        self.goto(0,0)
        self.aci -= 180
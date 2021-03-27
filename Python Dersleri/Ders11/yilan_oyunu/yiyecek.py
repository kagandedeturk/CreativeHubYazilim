

from turtle import Turtle
import random as rnd

class Yiyecek(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.yenile()
        


    def yenile(self):
        x = rnd.randint(-280,280)
        y = rnd.randint(-280,280)
        self.goto(x,y)
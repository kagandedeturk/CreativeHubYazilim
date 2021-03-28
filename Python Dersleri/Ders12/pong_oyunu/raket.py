

from turtle import Turtle

class Raket(Turtle):

    def __init__(self, pozisyon):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(pozisyon)

    def asagi_git(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)


    def yukari_git(self):   
        self.goto(self.xcor(), self.ycor() + 20)

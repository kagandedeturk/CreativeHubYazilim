
from turtle import Screen,Turtle
from yilan import Yilan
from yiyecek import Yiyecek
from skortahtasi import SkorTahtasi
import time


ekran = Screen()
ekran.setup(width=600, height=600)
ekran.bgcolor("black")

yilan = Yilan()

yemek = Yiyecek()
skorTahtasi = SkorTahtasi()

ekran.listen()
'''
ekran.onkey(yilan.sol, "Left")
ekran.onkey(yilan.sag, "Right")
ekran.onkey(yilan.yukari, "Up")
ekran.onkey(yilan.asagi, "Down")
'''
ekran.onkey(yilan.sol, "a")
ekran.onkey(yilan.sag, "d")
ekran.onkey(yilan.yukari, "w")
ekran.onkey(yilan.asagi, "s")

while True:
    yilan.hareket_et()
    time.sleep(0.1)

    # Yiyecek ile temasi tespit et

    if yilan.BAS.distance(yemek) < 15:
        yemek.yenile()
        skorTahtasi.skor_arttir()
    

ekran.exitonclick()



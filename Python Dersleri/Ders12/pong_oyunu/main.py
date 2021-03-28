
from turtle import Screen, Turtle
from raket import Raket
from top import Top
from SkorTahtasi import SkorTahtasi
import time

renkler = {
    'beyaz' : (1,1,1),
    'siyah' : (0,0,0)
}


ekran = Screen()
ekran.bgcolor(renkler['siyah'])
ekran.setup(height=600,width=800)
ekran.tracer(0)

sag_raket = Raket((350,0))
sol_raket = Raket((-350,0))
top = Top()
skorT = SkorTahtasi()

ekran.listen()

ekran.onkey(sag_raket.yukari_git,"Up")
ekran.onkey(sag_raket.asagi_git,"Down")
ekran.onkey(sol_raket.yukari_git,"w")
ekran.onkey(sol_raket.asagi_git,"s")




oyun_aktif_mi = True
while oyun_aktif_mi:
    ekran.update()
    time.sleep(0.05)
    top.hareket_et()


    # Topun duvarla temasini tespit eder ve yansimasini saglar
    if top.ycor() >= 290 or top.ycor() <= -290:
        top.yansima_yap()


    # Topun raketle temasini tespit eder ve yansimasini saglar
    if (top.distance(sag_raket) <= 50 and top.xcor() >= 330) or (top.distance(sol_raket) <= 50 and top.xcor() <= -330):
        top.yansima_yap()

    
    # top sag duvara geldiyse tespit et ve sol tarafin skorunu attir
    if top.xcor() > 380:
        top.basa_don()
        skorT.sol_skor_arttir()
        

    # top sol duvara geldiyse tespit et ve sag tarafin skorunu attir
    if top.xcor() < -380:
        top.basa_don()
        skorT.sag_skor_arttir()


ekran.exitonclick()


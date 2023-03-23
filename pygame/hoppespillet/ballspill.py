import pygame as pg
from ball import Spiller
from stolpe import Stolpe
import time

spiller1=Spiller()
hindere=[]

for i in range(3):
    nytt_hinder=Stolpe()
    hindere.append(nytt_hinder)


pg.init()
VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu=pg.display.set_mode([VINDU_BREDDE,VINDU_HOYDE])

fortsett=True
while fortsett:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            fortsett = False

    vindu.fill((150,25,105)) #farger bakgrunnen

    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)



    # pg.draw.rect(vindu, (30,70,125),(0,0,200,100))
    #pg.draw.rect(vindu, (r,g,b),(xpos,ypos,bredde,høyde))

    spiller1.tegn(vindu)
    # pg.draw.circle(vindu,(r,g,b),(xpos,ypos),radius)

    ballrect = spiller1.move((speedX,speedY))
    if ballrect.left < 0 or ballrect.right > width:
        speedX = -speedX
    if ballrect.top < 0 or ballrect.bottom > height:
        speedY = -speedY



    pg.display.flip() #oppdaterer pygame vinduet
    time.sleep(1/60)



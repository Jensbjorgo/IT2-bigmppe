# Example file showing a basic pygame "game loop"
import pygame
from hester import Hest
from random import randint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

hester=[]

# for i in range(3):
#     nyhest=Hest()
#     hester.append(nyhest)

hest1=Hest(500,(0,200,0))
hest2=Hest(400,(200,0,0))
hest3=Hest(300,(0,0,200))

pygame.display.set_caption('Horse betting')

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Grønn hest vant!', True,(100,50,1),(0,200,0))
text2=font.render('Rød hest vant!', True,(100,50,1),(200,0,0))
text3=font.render('Blå hest vant!', True,(100,50,1),(0,0,200))
vinn = font.render("den beste hesten vant", True,(100,50,1),(10,200,50))
textRect = text.get_rect()
textRect.center = (1280 // 2, 720 // 2)




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("white")

    pygame.draw.line(screen, ("black"), [1200+25, 0], [1200+25, 1000], 5) #Målstrek

    hest1.tegn(screen)
    hest2.tegn(screen)
    hest3.tegn(screen)

    tall= randint(1,3)
    if tall==1:
        hest1.flytt_hoyre(screen)
    elif tall==2:
        hest2.flytt_hoyre(screen)
    else:
        hest3.flytt_hoyre(screen)

    if hest1._x>1200 and hest2._x<1200 and hest3._x<1200:
        #screen.fill(hest1.farge)
        screen.blit(text,(1280//2,300))
    elif hest2._x>1200 and hest1._x<1200 and hest3._x<1200:
        #screen.fill(hest2.farge)
        screen.blit(text2,(1280//2,300))
    elif hest3._x>1200 and hest1._x<1200 and hest2._x<1200:
        #screen.fill(hest3.farge)
        screen.blit(text3,(1280//2,300))


    
        

    # LAG SPILLET DIT HER:

    #for hest in hester:
    #    hest.tegn(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()
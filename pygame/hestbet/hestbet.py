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

hest1=Hest(500,200,input("Vil du velge hest 3"))
hest2=Hest(400,100,input("Vil du velge hest 2"))
hest3=Hest(300,50,input("Vil du velge hest 1"))

pygame.display.set_caption('Horse betting')

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Velg din hest!', True,(100,50,1),(10,200,50))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("purple")

    

    hest1.tegn(screen)
    hest2.tegn(screen)
    hest3.tegn(screen)

    tall= randint(1,3)
    if tall==1:
        hest1.flytt_hoyre()
    elif tall==2:
        hest2.flytt_hoyre()
    else:
        hest3.flytt_hoyre()

    

    # LAG SPILLET DIT HER:

    # for hest in hester:
    #     hest.tegn(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    screen.blit(text)

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()
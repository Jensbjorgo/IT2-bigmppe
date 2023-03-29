
    # pg.draw.rect(vindu, (30,70,125),(0,0,200,100))
    #pg.draw.rect(vindu, (r,g,b),(xpos,ypos,bredde,høyde))
    # pg.draw.circle(vindu,(r,g,b),(xpos,ypos),radius)
import pygame
from ball import Spiller
from stolpe import Hinder

# pygame setup
pygame.init()
bredde = 1280 # bredden på vinduet
høyde = 720 # høyden på vinduet
vindu = pygame.display.set_mode((bredde, høyde))
klokke = pygame.time.Clock()
running = True
frames = 0

spiller1 = Spiller(høyde)
hindere = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    vindu.fill("purple") #farger bakgrunnen

    if frames == 180:
    # Hvis det har gått 180 frames / 3 sekunder:
        nytt_hinder = Hinder(bredde, høyde) # lag et nytt hinder-objekt
        hindere.append(nytt_hinder)  # legg det nye hinderet i listen over hindere
        frames = 0 # sett frames til å være 0

    # Flytter og tegner hindere:
    for hinder in hindere:
    # for hvert hinder i listen hindere:
        hinder.flytt()
        hinder.tegn(vindu)

    # Hopper hvis bruker trykker på mellomrom:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        spiller1.hopp()

    spiller1.fall() # spiller faller nedover
    spiller1.tegn(vindu) # tegner spiller

    frames += 1 # øker frames med 1

    pygame.display.flip() #oppdaterer pygame vinduet
    klokke.tick(60)  # begrenser FPS to 60

pygame.quit()
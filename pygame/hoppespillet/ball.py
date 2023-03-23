import pygame as pg

class Spiller:
    """Klasse som tegner ballen i hoppespillet
    
    """
    def __init__(self):
        self._x=20
        self._y=20

    def tegn(self,vindu):
        pg.draw.circle(vindu,(223,83,67),(self._x,self._y),25)
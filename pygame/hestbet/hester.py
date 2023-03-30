from random import randint
import pygame as pg

class Hest:
    """ Klasse som lager hestene i hestespillet
    
    """
    def __init__(self,y, farge):
        self.score=0
        self._x=1
        self._y=y
        self.farge=farge
    def vinn(self,vindu):
        vindu.fill(self.farge)

    def flytt_hoyre(self,vindu):
        
        if self._x>1200:
            self._x+=0
        else:
            self._x+=2

    def tegn(self,vindu):
        pg.draw.circle(vindu,(self.farge),(self._x,self._y),25)
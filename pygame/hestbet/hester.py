from random import randint
import pygame as pg

class Hest:
    """ Klasse som lager hestene i hestespillet
    
    """
    def __init__(self,y, farge, valg):
        self.score=0
        self._x=1
        self._y=y
        self.farge=farge
        self._valg=valg
    def vinn(self):
        if self._valg=="ja":
            self.score+=1

    def flytt_hoyre(self):
        if self._x<1200:
            self._x+=2
        else:
            self.vinn()

    def tegn(self,vindu):
        pg.draw.circle(vindu,(self.farge,100,0),(self._x,self._y),25)
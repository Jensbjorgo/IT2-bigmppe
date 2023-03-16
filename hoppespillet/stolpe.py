from random import randint

class Stolpe:
    def __init__(self):
        self._x=300
        self._hoyde=randint(20,40)
        self._y=500-self._hoyde
        self._bredde=10

    def flytt_venstre(self):
        self._x-=1


    def tegn(self,vindu):
        pg.draw.rect(vindu, (30,70,125),(self._x,self._y,self._bredde,self._hoyde))
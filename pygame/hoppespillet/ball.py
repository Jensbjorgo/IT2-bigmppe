
import pygame

class Spiller:
    """Klasse som tegner ballen i hoppespillet
    
    """
    def __init__(self, høyde_verden):
        self._x = 50
        self._høyde_verden = høyde_verden
        self._radius = 40
        self._y = høyde_verden - self._radius

    def tegn(self, vindu):
        pygame.draw.circle(vindu, "red", (self._x, self._y), self._radius)

    def hopp(self):
         self._y -= 10
    
    def fall(self):
        if self._y < self._høyde_verden - self._radius:
            self._y += 2
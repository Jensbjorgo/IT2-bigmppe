from random import randint

class Bilett():
    def __init__(self):
        self.mva=0.12
        self.pris=20

    def beregnpris(self):
        return self.pris + (self.pris*self.mva)


class Barnebilett(Bilett):
    def __init__(self):
        super().__init__()
        self.pris = self.pris * 0.5

class Vernepliktig (Bilett):
    def __init__(self):
        super().__init__()
        self.pris = self.pris * 0.1
class Ukebilett(Bilett):
    def __init__(self):
        super().__init__()
        self.pris = (self.pris * 7) * 0.8


voksen=Bilett()
barn=Barnebilett()
Jeg=Vernepliktig()
uke=Ukebilett()

print (voksen.beregnpris())
print (barn.beregnpris())
print(Jeg.beregnpris())
print(uke.beregnpris())


from random import randint

class Terning:
    def __init__(self,sider):
        self.sider=int(sider)

    def trillterning(self):
        svar=randint(1,self.sider)
        return svar

class Jukseterning(Terning):
    def __init__(self,sider,kast):
        super().__init__(sider)
        self.kast=kast

    def trillterning(self):
        hoy =-1
        for i in range(self.kast):
            kast = super().trillterning()
            if kast>hoy:
                hoy=kast
        
        return hoy
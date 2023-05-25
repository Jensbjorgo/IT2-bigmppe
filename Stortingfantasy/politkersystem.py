class Politiker:
    '''
    En klasse for politikere med navn, parti,fylke,fødselsdato og kjønn. 
    '''
    def __init__(self,navn, Parti,fylke,fdato,kjonn): #intruktør
        self._navn=navn
        self._parti=Parti
        self._fylke=fylke
        self._dato=fdato
        self._kjonn=kjonn
    def __str__(self):
        #en metode som bestemmer hvordan et objekt av denne klassen skal printes
        return f"{self._navn}({self._parti})"


class Parti:
    '''
    En klasse for partier med navn på partiet, politisk retning leder i partiet og liste over politikere som er medlem.
    '''
    def __init__(self, navn,retning):
        self._navn=navn
        self._retning=retning
        self._leder=None
        self._politkere=[]
    def __str__(self):
        return self._navn
    def sett_leder(self,leder):
        for politiker in self._politkere:
            if leder==politiker:
                self._leder=leder
                return f"{self._leder} er nå kapteinen av skipet!"
            return "Feil: politikeren er ikke med i partiet"
    def legg_til_politiker(self, politiker):
        self._politkere.append(politiker)
    def hent_leder(self):
        return self._leder
    def hent_politikere(self):
        return self._politkere
    

class Lag:
    '''
    Laget der politikerene skal spille. skal være maks 11 politikere.
    '''
    def __init__(self, politikerliste):
        self.lagliste=politikerliste
    def leggtilspiller(self,poloitiker):
        self.lagliste.append(poloitiker)
        if len(self.lagliste)>11:
            self.lagliste.remove(-1)


#eksperttips lager en ifsetning sjkekker om fila kjøres direkte
if __name__=="__main__":
    print("Test")
    jonas=Politiker("Jonas Gahr Støre", "AP", "Oslo", "1.2.22", "mann")
    print(jonas)
    ap=Parti("Arbeiderpartiet", "venstreorientert")
    ap.legg_til_politiker(jonas)
    ap.sett_leder(jonas)
    assert ap.hent_leder()==jonas
    print("Parti og politiker testing:OK!")



class Bruker:
    def __init__(self,lag):
        self.lag=lag
    
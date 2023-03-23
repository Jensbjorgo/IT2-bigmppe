class Bruker:
    """ superklasse for brukere i skolesystemet. Skal ikke bruke direkte.
    attributes:
        epost:enstring med brukers epost
        fornavn:en string med brukerns fornavn
        etternavn:en string med brukerns etternavn
    """
    def __init__(self,epost, fornavn,etternavn):
        self.epost=epost
        self.fornavn=fornavn
        self.etternavn=etternavn

    def logginn(self):
        print(f"{self.epost} logget inn")
    def loggut(self):
        print(f"{self.epost} logget ut")

class Laerer(Bruker):
    """ subklasse for lærere i skolesystemet.kan brukes direkte.
    attributes:
        epost:enstring med brukers epost
        fornavn:en string med brukerns fornavn
        etternavn:en string med brukerns etternavn
        lonn: lønnsnummeret til brukeren
    """
    def __init__(self,epost,fornavn,etternavn,lonn):
        super().__init__(epost,fornavn,etternavn)
        self.lonn=lonn



class Elev(Bruker):
    """ subklasse for elever i skolesystemet. kan brukes direkte.
    attributes:
        epost:enstring med brukers epost
        fornavn:en string med brukerns fornavn
        etternavn:en string med brukerns etternavn
        trinn: en string med hvilket trinn brukern er i
        klasse:en string med hvilken klasse brukern er i
        fag:en string med hvilket fag brukern er i
    """
    def __init__(self,epost,fornavn,etternavn,trinn, klasse,fag):
        super().__init__(epost,fornavn,etternavn)
        self.trinn=trinn
        self.klasse=klasse
        self.fag=fag

    def egenmelding(self):
        pass
        

Jens=Elev("snej765@gmail.com", "Jens","Bjørgo",3, "STA", "IT2")


if __name__ =="__main__":#brukes for å teste kode og kjøres kun dersom denne filen kjøres
    ravi=Laerer("Ravi@m.viken.no","Ravi","manikarnika",970034056654)
    Jens=Elev("snej765@gmail.com", "Jens","Bjørgo",3, "STA", "IT2")
    ravi.logginn()
    Jens.logginn()
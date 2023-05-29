from random import randint

class Pung:
    def __init__(self,navn,innhold):
        self.navn=navn
        self.innhold=innhold

    def gronn(self,innlegg):
        self.innlegg=innlegg
        self.innhold+= self.innlegg*14
        print(f"Det ble grønn du fikk {self.innlegg*14} og har tilsammen {self.innhold} totalt")
        return self.innhold

    def rod(self,innlegg):
        self.innlegg=innlegg
        self.innhold+= self.innlegg*2
        print(f"Det ble rød du fikk {self.innlegg*2} og har tilsammen {self.innhold} totalt")
        return self.innhold
    
    def svart(self,innlegg):
        self.innlegg=innlegg
        self.innhold+= self.innlegg*2
        print(f"Det ble svart du fikk {self.innlegg*2} og har tilsammen {self.innhold} totalt")
        return self.innhold

    def tap(self,innlegg):
        self.innlegg=innlegg
        self.innhold-=innlegg
        print(f"Det ble ikke det du valgte, du tapte {self.innlegg} og har tilsammen {self.innhold} totalt")
        return self.innhold
    
    def bet(self, innlegg,valg):
        farge = randint(1,1000)
        if farge<=28 and valg=="grønn":
            return self.gronn(innlegg)
        elif 28<farge<486+28 and valg=="rød":
            return self.rod(innlegg)
        elif farge>486+28 and valg=="svart":
            return self.svart(innlegg)
        else:
            return self.tap(innlegg)




fortsett=True
pung1= Pung("Jens",200)

while fortsett:
    pung1.bet(int(input("Hvor mye vil du legge inn? ")),input("hvilken farge? "))
    if pung1.innhold<=0:
        print("Du har ikke råd til å bette lenger..")
        fortsett=False
    if pung1.innhold>1000:
        print("Gratulerer du er tusionær! ")
    vil= input("Vil du prøve igjen? ")
    if vil=="nei":
        print("Du er velkommen tilbake en annen gang")
        fortsett=False
    

         




fil=open("1.samfunn og systemer/Standarder for lagring, utveksling og sikring av data/aa.csv")
data=fil.read()
linjer=data.split("\n")
#print(data)
#print(linjer)


class Person:
    def __init__(self, navn,alder,sted,skole):
        self._navn=navn
        self._alder=alder
        self._sted=sted
        self._skole=skole
    def __str__(self) -> str:
        return (f"{self._navn} er fra {self._sted} og går på {self._skole}")
    def hent_navn(self):
        return self._navn
    
class Skole:
    def __init__(self,navn):
        self._navn=navn
        self._elever=[]
    def legg_til_elev(self,elev):
        self._elever.append(elev)
    def hent_elever(self):
        for elev in self._elever:
            print (elev)



skoler={}
skoler2=[]

for linje in linjer:
    person=linje.split(",")
    navn=person[0]
    alder=person[1]
    sted=person[2]
    skole=person[3]
    if skole not in skoler:
        skoler[skole]=1
        ny_skole=Skole(skole)
        skoler2.append(ny_skole)
    else:
        skoler[skole]+=1
    ny_person=Person(navn,alder,sted,skole)
    #print(ny_person)
    ny_skole.legg_til_elev(ny_person)

for skol in skoler2:
    skol.hent_elever()
    
maks_verdi = max(skoler, key=skoler.get)
print(f"{maks_verdi} er skolen med flest av oss")




    

from politkersystem import Politiker
from politkersystem import Parti

fil= open("Stortingfantasy/stortinget.csv")
data=fil.read()
linjer=data.split("\n")

politikere=[]
partier=[]
opprettede_partier=[]


for linje in linjer[1:]:
    splittet_linje=linje.split(",")
    etternavn,fornavn,kjønn,fylke,parti=splittet_linje

    ny_politiker=Politiker(fornavn + " "+ etternavn,parti,fylke,"-", kjønn)
    politikere.append(ny_politiker)

    if parti not in opprettede_partier:
        nytt_parti=Parti(parti,"-")
        partier.append(nytt_parti)
        opprettede_partier.append(parti)

print(politikere[1])
print(partier[-1])




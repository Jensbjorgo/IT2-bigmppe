#3. Bruk filen `List of world cities by population density.csv` og finn ut hvilket land som har flest byer på topp-50 listen av byer med høyest befolkningstetthet.

fil = open("1.samfunn og systemer/Standarder for lagring, utveksling og sikring av data/liste.csv")
data = fil.read()
linjer = data.split("\n")


land={}
for linje in linjer:
    if linje:
        country = linje.split(",")[-1]
        land[country] = land.get(country, 0) + 1

print(land)
# Finn landet med flest byer i topp-50 listen
land_med_flest_byer = max(land, key=land.get)

print("--------------------------------")

print(f"Landet med flest byer i topp 50 er {land_med_flest_byer} med {land['India']}")
print("-------------------------------")
#4. Bruk filen AirBnb-Europe.csv og finn ut hvilken by som er billigst å leie leilighet i

fil2=open("1.samfunn og systemer/Standarder for lagring, utveksling og sikring av data/AirBnb-Europe.csv")
data2=fil2.read()
linjer2=data2.split("\n")

priser={}
for linje in linjer2[1:-1]:
    kolonne=linje.split(",")
    by=kolonne[0]
    pris=float(kolonne[1])
    if by in priser:
        priser[by].append(pris)
    else:
        priser[by]=[pris]

snitt={}
for by, verdier in priser.items():
    snittverdi=sum(verdier)/len(verdier)
    snitt[by]= snittverdi

minst=1000000
billigste_by= " "

for by,snittverdi in snitt.items():
    if snittverdi<minst:
        minst=snittverdi
        billigste_by=by
    print(f"Den gjennomsnittlige prisen i {by} er {snittverdi}")

print("------------------")
print(f"Den billigste byen er derfor {billigste_by} med en gjennomsnittsptis på {minst}")
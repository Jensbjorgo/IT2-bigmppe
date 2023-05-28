#3. Bruk filen `List of world cities by population density.csv` og finn ut hvilket land som har flest byer på topp-50 listen av byer med høyest befolkningstetthet.

import matplotlib.pyplot as plt

fil = open("samfunn og systemer/Standarder for lagring, utveksling og sikring av data/liste.csv")
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

print(f"Landet med flest byer i topp 50 er {land_med_flest_byer} med {land['India']}")
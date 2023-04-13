#3. Bruk filen `List of world cities by population density.csv` og finn ut hvilket land som har flest byer på topp-50 listen av byer med høyest befolkningstetthet.

import matplotlib.pyplot as plt

fil = open("Standarder for lagring, utveksling og sikring av data/List of world cities by population density.csv")
data = fil.read()
linjer = data.split("\n")


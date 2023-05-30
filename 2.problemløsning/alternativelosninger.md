# Alternative Løsninger
For å ikke sitte fast når du skal programmere er det viktig å kunne bruke alternative løsninger.

## Mulig løsning for et roulette spill
- [Roulettespill](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/diverse/Roulette.py)


## Forskjellige måter å åpne en csv-fil
python````

fil = open("tentamenmai/pokemon.csv") # åpner filen pokemon.csv
data = fil.read() # leser innholdet i filen
linjer = data.split("\n") # splitter innholdet på linjeskift, slik at linjer blir en liste med linjer


import csv

filnavn=("tentamenmai/pokemon.csv")

with open(filnavn,encoding="iso8859-1") as fil: # Åpner filen
    data = csv.reader(fil, delimiter=",")         # Leser inn data som csv



with open(filnavn,encoding="iso8859-1") as fil: # Åpner filen
    data = csv.DictReader(fil, delimiter=",")   # Leser inn data som csv men i ordbok




```
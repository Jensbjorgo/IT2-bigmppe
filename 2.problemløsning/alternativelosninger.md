# Alternative Løsninger
For å ikke sitte fast når du skal programmere er det viktig å kunne bruke alternative løsninger.

## Eksempel 1
Mulig løsning for et roulette spill..
- [Roulettespill](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/diverse/Roulette.py)

## Eksempel 2
Her har jeg laget et (litt uferdig) spill der man kan vedde på hester. Måten jeg har gjort det er at en variabel får en tilfeldig verdi mellom 1 og 3 som tilsvarer hver sin hest. Når variablen får verdien til tilsvarende hest vil den rykke forover. Dette vil skje kontinuerlig fram til de er i mål.

- [Hestespill](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/pygame/hestbet)


## Forskjellige måter å åpne en csv-fil


```python
fil = open("fil.csv") # åpner filen pokemon.csv
data = fil.read() # leser innholdet i filen
linjer = data.split("\n") # splitter innholdet på linjeskift, slik at linjer blir en liste med linjer


import csv

filnavn=("fil.csv")

with open(filnavn,encoding="iso8859-1") as fil: # Åpner filen
    data = csv.reader(fil, delimiter=",")         # Leser inn data som csv



with open(filnavn,encoding="iso8859-1") as fil: # Åpner filen
    data = csv.DictReader(fil, delimiter=",")   # Leser inn data som csv men i ordbok

```




# Innhenting av data
For å kunne presentere data må du kunne hente det fra et sted. I python bruker man ofte .json filer eller .csv filer for å hente ut data.

## Eksempel Json fil

```python
import json

filnavn = "fil.json"

with open(filnavn, encoding="utf-8") as fil:
  data = json.load(fil)

print(data)

```

## Eksempel Csv fil

- [Innhenting-av-data](https://github.com/Jensbjorgo/IT2-bigmppe/blob/main/1.samfunn%20og%20systemer/Standarder%20for%20lagring%2C%20utveksling%20og%20sikring%20av%20data/folketetthet.py)

## Eksempel i større prosjekt
Her har jeg laget en interaktiv nettsiden med flask der jeg henter ut data fra en json fil til en html nettside

- [Watford Nettside](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/diverse/Fifapack-kopi)
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

- [Innhenting-av-data](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/1.samfunn og systemer/Standarder for lagring, utveksling og sikring av data/folketetthet.py)
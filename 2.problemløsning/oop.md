# Objekorientert programmering
Programmering der man bruker klasser, arv, objekter og metoder.

## Eksempel

- [Hoppespill](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/pygame/hoppespillet)

## Eksempel 2
- [Storting Fantasy](https://github.com/Jensbjorgo/IT2-bigmppe/tree/main/Stortingfantasy)

## Klasse
En klasse er en mal eller oppskrift på et objekt.

```python
class Katt:
    def __init__(self, navn, alder, farge),:
        self.navn = navn
        self.alder = alder
        self.farge = farge
    
    def spis(self):
        print(f"{self.navn} spiser lasagne!")

```

## Metode
Metoder er funkjsoner inni en klasse. På eksempelet om klasser er mjau() og init() eksepler på metoder.

## Objekt
Objekt er det som blir laget av klassen og som har egenskapene til klassen og metodene. 

```python
pusur=Katt("Pusur", 45, "Oransje")
print(pusur.farge)
pusur.spis()

```
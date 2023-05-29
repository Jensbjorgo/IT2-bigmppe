# vern mot kjøretidsfeil og logiske feil i programmer

håndtering av kjøretidsfeil i python gjøres med nøkkelordene try og except
python forsøker å kjøre kodeblokken under `try`, hvis python får en feilmelding vil den kjøre kodeblokken so ligger under `except:`

## eksempel

```python
while True:
    try:
        alder= int(input( "fødselsår.."))
        break
    except:
        print("alder må være heltall...")

fodsel= 2023-alder
print(f"år:{fodsel}")

```

## Eksperttips: While-løkke med try-except

```python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```

## Logiske feil i programmer

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet `assert` for å forsikre oss om at koden gir korrekte resultat.

Eksempel:

```python
assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting
assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmelding
```

Eksempel: Test av funksjoner med assert

```python
def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14
```

### Eksperttips: Håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("Alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
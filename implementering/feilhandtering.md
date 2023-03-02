#vern mot kjøretidsfeil og logiske feil i programmer

håndtering av kjøretidsfeil i python gjøres med nøkkelordene try og except
python forsøker å kjøre kodeblokken under `try`, hvis python får en feilmelding vil den kjøre kodeblokken so ligger under `except:`


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
# Plotting
Plotting er en form for presetasjon av data i python. ved å importere fra "matplotlib.pyplot". Alt du trenger er en form for data og "plt.plot"

## Eksempel 1

```python
import matplotlib.pyplot as plt

xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

plt.scatter(xverdier, yverdier)  # Lager grafen
plt.show()                       # Viser grafen
```

## Eksempel 2

```python
import matplotlib.pyplot as plt

def f(x):
  return x**2

xverdier = [xverdi for xverdi in range(10)]
yverdier = [f(xverdi) for xverdi in xverdier]

plt.plot(xverdier, yverdier)
plt.show()
```
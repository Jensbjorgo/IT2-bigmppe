# Gjenbrukbar kode

kode som kan bruker igjen og igjen ofte i samme program. Ved å bruke gjenbrukbar kode sparer vi tid og minsker risikoen for feil


## et eksempel på en lett gjenbrukbar kode
```python
def sihei(navn):
    print(f"Hei {navn} velkommen!")

sihei("Thor")
sihei("Peder")


```
## eller

```python
def gjsn(liste):
    summen=sum(liste)
    svar=summen/len(liste)
    return svar

liste1=[5,4,3,2,1]
liste2=[10,20,30,40]

gjsn(liste1)
gjsn(liste2)

```

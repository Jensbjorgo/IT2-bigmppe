
from email.mime import image
import imghdr
from posixpath import split
from flask import Flask, render_template
import json
from random import seed
from random import randint

app = Flask(__name__)

fil = open("players.json", encoding="utf-8")
kortliste = json.load(fil)

samleliste = []

fattig = " "
fattig2 = " "
fattig3 = " "

def slett(id):
    nummer = int(id) - 1
    samleliste.pop(nummer)
    
bank=0

#Hjemmeside

@app.route("/")
def index():

    return render_template("index.html", kortliste=kortliste, samleliste=samleliste)



#Pakkeåpning

@app.route("/<id>")
def open(id):
    kortnummer = int(id) + randint(0,749)
    kortnummer2 = randint(0,750)
    kortnummer3 = randint(0,750)
    kortnummer4 = randint(0,750)
    samleliste.append(kortliste[kortnummer]["player_name"]+ " " + str( kortliste[kortnummer]["overall"]))
    samleliste.append(kortliste[kortnummer2]["player_name"]+ " " + str( kortliste[kortnummer2]["overall"]))
    samleliste.append(kortliste[kortnummer3]["player_name"]+ " " + str( kortliste[kortnummer3]["overall"]))
    samleliste.append(kortliste[kortnummer4]["player_name"]+ " " + str( kortliste[kortnummer4]["overall"]))
    
    print(samleliste)


    return render_template("open.html", kortliste=kortliste, kortnummer=kortnummer, kortnummer2=kortnummer2, kortnummer3=kortnummer3,kortnummer4=kortnummer4,samleliste=samleliste )
    



#Dine spillere

@app.route("/dine")
def dine():

    return render_template("dine.html", samleliste=samleliste, bank=bank, kortliste=kortliste)

@app.route("/slett/<id>")
def slettid (id):
    global bank
    nummer = int(id) - 1
    overall = int(samleliste[nummer].split(" ")[-1])
    if overall > 90:
        bank = bank+10000
    else:
        bank += 500
    
    slett(id)
    
    return dine()




# Spillerene du mangler

@app.route("/po")
def po():
    global samleliste
    global kortliste
    mangler = []
    for kort in kortliste:
        if kort not in samleliste:
            mangler.append(kort)
    return render_template("potensiell.html", kortliste=kortliste,samleliste=samleliste, mangler=mangler, kort=kort)


@app.route("/po/<League>")
def info(League):
    global kortliste
    sortert=[]
    for kort in kortliste:
        if kort["league"]==League:
            sortert.append(kort)

    return render_template("potensiell.html", kortliste=sortert)


#Shop


@app.route("/buy")
def buy():
    global bank
    global fattig
    global fattig2
    global fattig3
    fattig = " "
    fattig2 = " "
    fattig3 = " "


    return render_template("shop.html", bank=bank, kortliste=kortliste, fattig=fattig)
@app.route("/add")
def add():
    global bank
    global fattig
    if bank > 10000:
        samleliste.append(kortliste[3]["player_name"]+ " " + str(kortliste[3]["overall"]))
        bank=bank-10000
    else:
        fattig="Du er for fattig for dette ass"



    return render_template("shop.html", bank=bank, kortliste=kortliste, fattig=fattig)

@app.route("/add2")
def add2():
    global bank
    global fattig2
    if bank > 50000:
        samleliste.append(kortliste[749]["player_name"]+ " " + str(kortliste[749]["overall"]))
        bank=bank-50000
    else:
        fattig2="Du er for fattig for dette ass"



    return render_template("shop.html", bank=bank, kortliste=kortliste, fattig2=fattig2)

@app.route("/add3")
def add3():
    global bank
    global fattig3
    if bank > 200:
        samleliste.append(kortliste[275]["player_name"]+ " " + str(kortliste[275]["overall"]))
        bank=bank-200
    else:
        fattig3="Du har ikke råd til martin engang😭"



    return render_template("shop.html", bank=bank, kortliste=kortliste, fattig3=fattig3)
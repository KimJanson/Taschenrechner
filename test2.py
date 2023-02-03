import re

def rechner():
    eingabe = input("Ihre Eingabe: ")

    match = re.search("^\d+[\*\+\-/]\d+$", eingabe)

    if not match:
        print("!!!Ungültiges Zeichen!!!")
        return
        
    if "+" in eingabe:
        eingaben = eingabe.split ("+")
    if "-" in eingabe:
        eingaben = eingabe.split ("-")
    if "*" in eingabe:
        eingaben = eingabe.split ("*")   
    if "/" in eingabe:
        eingaben = eingabe.split ("/")

    zahl1 = int(eingaben[0]) 

    zahl2 = int(eingaben[1]) 
 
    if "+" in eingabe:
        ergebnis = zahl1 + zahl2
    if "-" in eingabe:
        ergebnis = zahl1 - zahl2
    if "*" in eingabe:
        ergebnis = zahl1 * zahl2
    if "/" in eingabe:
        ergebnis = zahl1 / zahl2 

    print("Das Ergebnis ist " + str(ergebnis))

while True:
    rechner()
    eingaben1 = input("Weitere Eingabe? (ja/nein): ")
    if eingaben1 == "nein":
        break
    elif eingaben1 != "ja":
        print("!!!Ungültiges Zeichen!!!")
        break

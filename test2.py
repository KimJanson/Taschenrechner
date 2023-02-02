import re

def rechner():
    eingabe = input("Ihre Eingabe: ")

x = re.search("^\d+[\*\+\-/]\d+$", txt)
    if "+", "-", "*","/" in eingabe:
        eingaben = eingabe.split ("+", "-", "*", "/")
    else:
        print("Ungültige Eingabe")
        
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
    x = re.search("^\d+[\*\+\-/]\d+$", eingaben)
    if x:
        continue
    else:
        print("Ungültige Eigabe")

    rechner()
    eingaben1 = input("Weitere Eingabe? (ja/nein): ")
    if eingaben1 == "nein":
        break
else:
    print("Ungültiges Zeichen")

eingabe = input("Ihre Eingabe: ")

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

frage = input("Willst du weiter rechnen? (Ja/Nein): ")

frage = str(jein)

if (jein == "Ja"):
    
elif (jein == "Nein"):            

print("Das Ergebnis ist " + str(ergebnis))

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

print("Das Ergebnis ist " + str(ergebnis))

eingaben1 = input("Weitere Eingabe?: ")
  
for x in eingaben1:
  if x == "ja":
    continue

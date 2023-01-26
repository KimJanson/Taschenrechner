eingabe = input("Ihre Eingabe: ")

eingaben = eingabe.split ("+")
eingaben1 = eingabe.split("-")

zahl1 = int(eingaben[0]) 
zahl2 = int(eingaben[1])  

ergebnis = zahl1 + zahl2
print("Das Ergebnis ist " + str(ergebnis))
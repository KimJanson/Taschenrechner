Zahl1 = int(input("1.Zahl: "))
Zahl2 = int(input("2.Zahl: "))
Rechenzeichen = input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")
if Rechenzeichen == "+":
    Ergebnis=Zahl1+Zahl2
if Rechenzeichen == "-":
    Ergebnis=Zahl1-Zahl2
if Rechenzeichen == "*":
    Ergebnis=Zahl1*Zahl2
if Rechenzeichen == "/":
    Ergebnis=Zahl1/Zahl2    
print("Das Ergebnis ist: " + str(Ergebnis))  

nächste_rechnung = input("Möchten sie noch eine Rechnung machen? (ja/nein): ")
        if nächste_rechnung == "nein" :
          break

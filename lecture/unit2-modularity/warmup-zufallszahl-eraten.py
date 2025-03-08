import random

zahl = random.randint(1, 100)

ratezahl = -100
while ratezahl != zahl:
    ratezahl = int(input("Bitte Zahl eingeben: "))
    if ratezahl > zahl:
        print("Die Zahl ist zu gross...")
    elif ratezahl < zahl:
        print("Die Zahl ist zu klein...")

print("Herzlichen Glückwunsch - die Zahl ist korrekt.")



from json import dump, load, dumps, loads

produkte = [{"name": "Apfel", "preis": 2.99, "land": "ch"}, 
            {"name": "Birne", "preis": 3.99, "land": "es"},
            {"name": "Kirsche", "preis": 5.99, "land": "at"}]

# while True:
#     produkt = input("Bitte Produkt eingeben (oder x für Exit): ")
#     if produkt == "x":
#         break
#     produkte.append(produkt)

with open("obst.json", "w") as f:
    dump(produkte, f)



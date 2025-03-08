lagerbestand = [
    { 'name': 'Notebook', 'anzahl': 10, 'preis': 1000 },
    { 'name': 'Maus', 'anzahl': 100, 'preis': 20 },
    { 'name': 'Tastatur', 'anzahl': 50, 'preis': 50 },
]

def berechne_lagerwert(lagerbestand):
    gesamtwert = 0
    for produkt in lagerbestand:
        gesamtwert += produkt['anzahl'] * produkt['preis']
    return gesamtwert

lagerwert = berechne_lagerwert(lagerbestand)
print(f"Der Gesamtwert des Lagerbestands beträgt: {lagerwert} Franken")


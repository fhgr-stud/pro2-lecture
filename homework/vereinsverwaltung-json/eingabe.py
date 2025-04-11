import json

# Beispiel Datenstruktur
mitglieder = {
    "001": {
        "name": "Max Mustermann",
        "eintrittsdatum": "2022-01-01",
        "geburtsdatum": "1990-05-12",
        "beitrag_bezahlt": True
    },
    "002": {
        "name": "Erika Musterfrau",
        "eintrittsdatum": "2023-03-15",
        "geburtsdatum": "1985-08-22",
        "beitrag_bezahlt": False
    },
    "003": {
        "name": "Lukas Beispiel",
        "eintrittsdatum": "2021-09-10",
        "geburtsdatum": "1995-11-30",
        "beitrag_bezahlt": True
    }
}


# Jetzt mit einlesen
mitglieder = {}
while True:
    id = input("Mitgliedernummer: ")
    if id == 'x':
        break

    name = input("Name: ")
    eintrittsdatum = input("Eintrittsdatum: ")
    geburtsdatum = input("Geburtsdatum: ")
    beitrag_bezahlt = bool(input("Mitgliedsbeitrag bezahlt (True/False): "))

    mitglieder[id] = {"name": name,
                      "eintrittsdatum": eintrittsdatum,
                      "geburtsdatum": geburtsdatum,
                      "beitrag_bezahlt": beitrag_bezahlt}

# speichern
with open("mitglieder.json", "w") as f:
    json.dump(mitglieder, f)





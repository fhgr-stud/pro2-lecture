import json

print("Mitgliederliste:")
with open("mitglieder.json", "r") as f:
    mitglieder = json.load(f)
    for nr, mitglied in mitglieder.items():
        print(f"{nr}: {mitglied['name']}, Eintrittsdatum: {mitglied['eintrittsdatum']}, "
              f"Geburtsdatum: {mitglied['geburtsdatum']}, "
              f"Mitgliedsbeitrag: {'bezahlt' if mitglied['beitrag_bezahlt'] else 'nicht bezahlt'}")





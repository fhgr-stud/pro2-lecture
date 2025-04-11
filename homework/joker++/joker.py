from flask import Flask, request
from random import randint

app = Flask(__name__)

def korrekte_stellen(joker, zahl):
    anzahl_korrekt = 0
    for index in range(5,-1,-1):
        if joker[index] != zahl[index]:
            break
        anzahl_korrekt = anzahl_korrekt + 1

    return anzahl_korrekt


def is_gueltig(zahl):
    return len(zahl) == 6 and zahl.isdigit()


def auswertung(zahl):
    joker = f"{randint(0,999999):06d}"
    if not is_gueltig(zahl):
        return "Ungültige Eingabe - die Zufallszahl muss aus 6 Ziffern bestehen."

    anzahl_korrekt = korrekte_stellen(joker, zahl)
    if anzahl_korrekt == 0:
        return f"Zufallszahl {joker} - leider keine Übereinstimmung in den Endziffern"
    elif anzahl_korrekt == 1:
        return f"Zufallszahl {joker} - Gratulation! Die letzte Endziffer stimmt überein"
    else:
        return f"Zufallszahl {joker} - Gratulation! Die letzten {anzahl_korrekt} Endziffern stimmen überein"


@app.route('/bet/<zahl>')
def bet(zahl):
    return auswertung(zahl)

@app.route('/wette')
def wette():
    zahl = request.args.get('zahl')
    return auswertung(zahl)



if __name__ == '__main__':
   app.run(debug=True, port=5000)

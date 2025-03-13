from random import randint

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/wetten', methods=['POST'])
def wette_abgeben():
   zahl = request.form['zahl']
   joker = f"{randint(0,999999):06d}"
   meldung = "Gewinn unbekannt"
   # TODO: prüfen, ob E-Mail-Adresse gültig
   # TODO: Daten speichern
   return render_template('feedback.html',       
                          zahl=zahl, joker=joker, meldung=meldung)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, redirect, request, make_response
from database import add_person, get_persons
import json

# App-Objekt erstellen
app = Flask('NewsletterApp')


# Startseite
@app.route('/')
def index():
    return render_template('index.html')

# Anmeldeformular verarbeiten
@app.route('/anmelden', methods=['POST'])
def anmeldung():
    # Daten aus dem Formular holen
    name = request.form['name']
    email = request.form['email']
    firma = request.form['firma']
    kanton = request.form['kanton']

    # ein möglicher, aber noch nicht ausreichender Test auf eine gültige E-Mail-Adresse
    if '@' not in email:
        return "Keine gültige E-Mail", 400

    # Ergebnisseite anzeigen
    add_person(email, name, firma, kanton)
    return render_template('anmeldung.html', email=email, name=name, firma=firma, kanton=kanton)

# Adminseite, zeigt alle Abonnenten an
@app.route('/admin')
def admin():
    daten = get_persons()
    return render_template('admin.html', daten=daten)

# Starten der Anwendung
app.run(debug=True)

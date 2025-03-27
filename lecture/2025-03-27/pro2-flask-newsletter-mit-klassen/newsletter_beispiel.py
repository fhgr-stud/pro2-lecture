from flask import Flask, render_template, redirect, request, make_response
import json

# App-Objekt erstellen
app = Flask('NewsletterApp')

class Person:
    def __init__(self, name, email, firma, kanton):
        self.name = name
        self.email = email
        self.firma = firma
        self.kanton = kanton


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

    person = Person(name, email, firma, kanton)

    # ein möglicher, aber noch nicht ausreichender Test auf eine gültige E-Mail-Adresse
    if '@' not in email:
        return "Keine gültige E-Mail", 400

    # Ergebnisseite anzeigen
    return render_template('anmeldung.html', person=person)

# Adminseite, zeigt alle Abonnenten an
@app.route('/admin')
def admin():
    daten = laden()
    return render_template('admin.html', daten=daten)

# Starten der Anwendung
app.run(debug=True)

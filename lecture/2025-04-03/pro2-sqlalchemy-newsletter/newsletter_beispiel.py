from flask import Flask, render_template, redirect, request, make_response, session
from database import add_person, get_persons

# App-Objekt erstellen
app = Flask('NewsletterApp')
app.secret_key="53d5b0ac-62d4-4500-9809-a7d0bfe13f24"

users = {
    'admin@fhgr.ch': b'$2b$12$lkkZ29opeNNSxKFDy8y0e.ct9fbuRSMFvtSpGr.y8kNP6StT//tga', # alpha
    'admin@wu.at': b'$2b$12$sgi8Q.DfeHfO6WIDW0jS9egoexx5F1Q5izx83zjtFVrbBsPpoyTKu'    # beta
}

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
    return render_template('anmeldung.html',
                           email=email, name=name, firma=firma, kanton=kanton)

# Adminseite, zeigt alle Abonnenten an
@app.route('/admin')
def admin():
    if 'user' in session:
        daten = get_persons()
        return render_template('admin.html', daten=daten)
    else:
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

# Starten der Anwendung
app.run(debug=True)

# Flask imports
from flask import Flask, render_template

# unser App-Objekt
app = Flask(__name__)

produkte = {
    1: {
        'name': 'Apfel',
        'preis': 1.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Pink_lady_and_cross_section.jpg'
    },
    2: {
        'name': 'Birne',
        'preis': 2.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Pears.jpg'
    },
    3: {
        'name': 'Kiwis',
        'preis': 3.99,
        'bild': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Apteryx_mantelli_-Rotorua%2C_North_Island%2C_New_Zealand-8a.jpg/2560px-Apteryx_mantelli_-Rotorua%2C_North_Island%2C_New_Zealand-8a.jpg'
    }
}

@app.route('/')
def home():
    return render_template('home.html', produkte=produkte)
    
@app.route('/produkt/<id>')
def details(id):
    if not id.isdigit() or int(id) not in produkte:
        return "Invalid product id: " + id, 300
    produkt = produkte[int(id)]
    return render_template('details.html', produkt=produkt)

# Server auf Port 3000 starten
if __name__ == '__main__':
    app.run(debug=True, port=5000)

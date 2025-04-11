# Flask imports
from flask import Flask, render_template, request
from random import randint

# unser App-Objekt
app = Flask(__name__)
zahl = randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def home():
    geraten = int(request.form.get('geraten', 0))
    return render_template('home.html', zahl=zahl, geraten=geraten)

@app.route('/newdigit')
def new():
    global zahl
    zahl = randint(1, 100)
    return render_template('home.html', zahl=zahl, geraten=0)
    
# Server auf Port 3000 starten
if __name__ == '__main__':
    app.run(debug=True, port=5000)

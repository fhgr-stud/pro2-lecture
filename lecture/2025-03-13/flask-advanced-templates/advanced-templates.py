from flask import Flask, \
   render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/enumerate')
def enumerate():
    fruits = ['Äpfel', 'Birnen', 'Trauben']
    return render_template('enumeration.html', fruits=fruits)

@app.route('/dictionary')
def dictionary():
    persons = [{ "name": "Max", "alter": 25,
                 "hobbies": ["Fussball", "Tennis"] },
               { "name": "Zoe", "alter": 22,
                 "hobbies": ["Schwimmen", "Tennis"] },
              ]
    return render_template('dictionary.html', persons=persons)

@app.route('/verzweigung/<person_name>')
def verzweigung(person_name):
    persons = {'Anna': {"name": "Anna", "hatGA": True},
               'Jim': {"name": "Jim", "hatGA": False}
              }
    if person_name in persons:
        return render_template('verzweigung.html', person=persons[person_name])
    else:
        return "Unbekannte Person", 404

if __name__ == '__main__':
   app.run(debug=True, port=5000)

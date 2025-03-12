from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/anmelden', methods=['POST'])
def anmelden():
   email = request.form['email']
   # TODO: prüfen, ob E-Mail-Adresse gültig
   # TODO: Daten speichern
   return render_template('feedback.html',       
                          email=email)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask           # Wir importieren Flask
from random import randint
app = Flask("Hello world app")    # Wir erzeugen ein App-Objekt mit dem
                                  # Namen „Hello world app“

# Eine Annotation – Zusatzinfo für die Funktion
@app.route('/')
def hello_world():                # Wir definieren eine Funktion, die 
   return "Hello world!"          # einen Text an den Browser liefert
                                  # und legen fest, dass der Pfad der URL 
                                  # “/“ sein soll (unsere Startseite).

@app.route('/random')
def random():      
   zufall = randint(1,10)
   return str(zufall)             # Wichtig - Rückgabewerte müssen immer Strings sein
                                  
if __name__ == '__main__':        # In dieser Zeile wird der mitgelieferte 
   app.run(debug=True, port=5000) # Server von Flask gestartet - dabei 
                                  # wird der Debug-Modus eingeschaltet und 
                                  # der Port auf 5000 festgelegt.

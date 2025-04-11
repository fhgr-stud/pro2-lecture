#
# Standard Template, um eine Flask Applikation zu erstellen
# Empfehlung: fügen Sie dies Ihrem Cheat-Sheet hinzu.
#
from flask import Flask, render_template, make_response, request

app = Flask(__name__)    


personen = { 
              1: {"name": "Ana", "wohnort": "Chur", 
                  "hobbies": ["Tanzen", "Joggen"]},
              2: {"name": "Jim", "wohnort": "Basel", 
                  "hobbies": ["Schwimmen"]},
              3: {"name": "Zoe", "wohnort": "Bern", 
                  "hobbies": ["Joggen", "Judo", "Jujitsu"]},
            }


@app.route('/', methods=["GET"])
def index():          
    return render_template("personen.html", personen=personen)

                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5000) 

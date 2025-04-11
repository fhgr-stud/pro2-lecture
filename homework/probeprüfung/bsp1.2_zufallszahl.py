#
# Standard Template, um eine Flask Applikation zu erstellen
# Empfehlung: fügen Sie dies Ihrem Cheat-Sheet hinzu.
#
from flask import Flask, render_template, make_response, request

app = Flask("Workflow")    

@app.route('/', methods=["GET"])
def index():          
    from random import randint
    zahl = randint(1, 6)     
    return str(zahl)
    # return f"{zahl}"    # Alternative

                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5000) 

#
# Standard Template, um eine Flask Applikation zu erstellen
# Empfehlung: fügen Sie dies Ihrem Cheat-Sheet hinzu.
#
from flask import Flask, render_template, make_response, request

app = Flask("Workflow")    

@app.route('/')
def index():               
    return "Hallo world :)"

                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5004)

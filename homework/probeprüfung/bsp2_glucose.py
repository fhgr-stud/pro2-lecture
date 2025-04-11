# bsp2_glucose.py
import health
from flask import Flask, render_template, make_response, request

app = Flask("Workflow")    

@app.route('/', methods=["GET", "POST"])
def index(): 
    messwert = request.form.get("messwert")
    if messwert:
        ergebnis = round(health.zu_mg_dl(float(messwert)), 2)
    else:
        ergebnis = None
    return render_template("eingabe.html", mg=ergebnis)

                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5000)

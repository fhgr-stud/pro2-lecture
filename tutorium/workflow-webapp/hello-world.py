from flask import Flask, render_template, make_response, request

app = Flask("Workflow")    

@app.route('/')
def index():               
    return "Hallo world :)"

@app.route('/chur', methods=["GET", "POST"])
def chur():
    if "name" in request.form:
        name = request.form["name"]
    else:
        name = ""
    return render_template("name.html", name=name)   # Name, willkommen in Chur


# http://localhost:5001?name=Ana
@app.route('/basel')
def basel():
    name = request.args.get('name')
    return f"{name} willkommen in Basel!"

# http://localhost:5001/bern/Anita
@app.route('/bern/<name>')
def bern(name):
    return f"{name} willkommen in Basel!"


                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5002) 

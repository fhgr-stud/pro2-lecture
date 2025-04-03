from flask import Flask, render_template, make_response, request

app = Flask("Workflow")    

@app.route('/')
def index():               
    return "Hallo world :)"
                                 
if __name__ == '__main__':        
   app.run(debug=True, port=5000) 

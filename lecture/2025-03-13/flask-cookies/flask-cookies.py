from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def count():
   # Cookie lesen, Anzahl erhöhen
   count = request.cookies.get('count', 0)
   count = int(count) + 1   # Vorsicht, Cookies sind immer Strings!

   # Response generieren
   response = make_response(f'{count} Besuche')
   response.set_cookie('count', str(count))
   return response

if __name__ == '__main__':
   app.run(debug=True, port=5000)

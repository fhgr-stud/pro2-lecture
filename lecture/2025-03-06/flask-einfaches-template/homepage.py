from flask import Flask, \
   render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')


@app.route('/about/')
def about():
   return render_template('about.html')

@app.route('/profile/<user>')
def profile(user):
   email = user + "@my.com"
   return render_template('profile.html',
                          user=user, email=email)

if __name__ == '__main__':
   app.run(debug=True, port=5001)

from flask import render_template
from application import app

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group='Everyone')

#### DO THIS WEDNESDAY #####
@app.route('/practise')
def practise():
    return render_template('practise.html', title='Practise')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About Us')

@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='Favourites',  favourites=["Cooking", "Drawing", "Traveling","Dancing"])

@app.route('/')
def index():
    return "Hello from Flask!"
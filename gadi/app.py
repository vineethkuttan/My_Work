import webbrowser
from flask import Flask,render_template
from ptable import petrol_price
from dtable import diesel_price

app = Flask(__name__)
diesel_price()
petrol_price()
@app.route('/')
@app.route('/home')
def home():   
    return render_template('home.html')

@app.route('/help')
def help():   
    return render_template('help.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():   
    return render_template('register.html')

@app.route('/about')
def about():   
    return render_template('about.html')

@app.route('/contact')
def contact():   
    return render_template('contact.html')

@app.route('/petrolprice')
def petrolprice():
    return render_template('petrolprice.html')


@app.route('/dieselprice')
def dieselprice():
    return render_template('dieselprice.html')

if __name__ == '__main__':
    app.run(debug=True,port=2323)


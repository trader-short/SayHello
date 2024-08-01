from flask import Flask, render_template, flash, request

app = Flask(__name__)
#add app.secret_key here


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/")
def hello():
    flash("What's your name?")
    return render_template('hello.html')

@app.route("/hello/greet",methods=['POST','GET'])
def greet():
    flash("Hi " + str(request.form['name_input']) + " ,great to see you!")
    return render_template('hello.html')
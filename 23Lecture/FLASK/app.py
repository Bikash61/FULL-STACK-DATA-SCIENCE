## Create a simple flask application
from flask import Flask, render_template, request, redirect , url_for

## Create the app flask 
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/welcome')
def welcome():
    return " <h1> Welcome to the fast Tutorial <h1> "

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/sucess/<int:score>')
def sucess(score):
    return "The person is passed and the score is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and the score is "+ str(score)

@app.route('/calculate',methods = ['POST','GET'])
def calculate():
    if request.method =='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
    average_marks = (maths+science+history)/3

    return render_template('result.html', result = average_marks)




    



if __name__ == '__main__':
    app.run(debug=True)
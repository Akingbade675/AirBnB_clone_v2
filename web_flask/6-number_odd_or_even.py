#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''root => displays Hello HBNB'''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    '''displays HBNB'''
    return "HBNB"


@app.route('/c/<text>')
def ctext(text):
    '''display C followed by the value of the text variable'''
    return "C %s" % text.replace('_', ' ')


@app.route('/python', defaults={'text': "is cool"})
@app.route('/python/<string:text>')
def python(text):
    '''prints Python is cool'''
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    '''displays n if integer'''
    return "%i is a number" % n


@app.route('/number_template/<int:n>')
def num_template(n):
    '''display a HTML page only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_or_even(n):
    '''display a HTML page only if n is an integer'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

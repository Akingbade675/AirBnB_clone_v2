#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask

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
@app.route('/python/<text>')
def python(text):
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

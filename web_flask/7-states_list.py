#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def list_states():
    '''Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    '''
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    '''remove the current SQLAlchemy session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

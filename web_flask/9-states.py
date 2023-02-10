#!/usr/bin/python3
'''starts a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    '''Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    '''
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    '''Displays an HTML page with info about <id>, if it exists.'''
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    '''remove the current SQLAlchemy session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

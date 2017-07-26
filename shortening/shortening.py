import os
from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    #DATABASE=os.path.join(app.root_path, 'shortening.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('SHORTENING_SETTINGS', silent=True)

# VIEWS

@app.route('/')
def show_entries():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print ('Launching with settings:', os.environ['APP_SETTINGS'])

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
    return 'Welcome to Shortening'

if __name__ == '__main__':
    app.run(debug=True)
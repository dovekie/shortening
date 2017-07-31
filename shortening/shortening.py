from datetime import datetime
import hashlib
import os
from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print ('Launching with settings:', os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

app.config.update(dict(
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('SHORTENING_SETTINGS', silent=True)

# VIEWS

@app.route('/', methods=['GET'])
def show_entries():
    return 'Welcome to Shortening'

@app.route('/', methods=['POST'])
def hash_it():
	hashed_url = unique_hash(request.form['url'])
	return hashed_url

if __name__ == '__main__':
    app.run(debug=True)

# HELPER FUNCTIONS

def unique_hash(str_input):
    d = datetime.now().isoformat()
    hashable = str_input + d
    hash_object = hashlib.md5(b'{}'.format(hashable))
    return hash_object.hexdigest()
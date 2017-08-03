from datetime import datetime
import hashlib
import os
from flask import (Flask, request, session, g, redirect, url_for, abort, 
     render_template, flash)
from flask_sqlalchemy import SQLAlchemy
from model import Surl, connect_to_db
from model import db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print ('Launching with settings:', os.environ['APP_SETTINGS'])

app.config.update(dict(
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('SHORTENING_SETTINGS', silent=True)
connect_to_db(app)

# VIEWS

@app.route('/', methods=['GET'])
@app.route('/<surl>', methods=['GET'])
def show_entries(surl=None):
    if surl:
        entry = Surl.query.filter_by(short_url=surl).first()
        if entry:
            print entry
            if accessed_today(entry.last_accessed):
                entry.day_count += 1
            else:
                entry.day_count = 1
            if accessed_this_week(entry.last_accessed):
                entry.week_count += 1
            else:
                entry.week_count = 1
            entry.last_accessed = datetime.now()
            entry.all_time_count += 1
            db.session.commit()
            return entry.url

    return 'Welcome to Shortening'

@app.route('/', methods=['POST'])
def hash_it():
    hashed_url = unique_hash(request.form['url'])
    new_surl = Surl(url=request.form['url'],
                    short_url=hashed_url,
                    last_accessed=datetime.now(),
                    day_count=1,
                    week_count=1,
                    all_time_count=1)
    print 'Adding a new entry:', new_surl
    db.session.add(new_surl)
    db.session.commit()
    return hashed_url

# HELPER FUNCTIONS

def unique_hash(str_input):
    """Create a unique hash from an input string
    """
    d = datetime.now().isoformat()
    hashable = str_input + d
    hash_object = hashlib.md5(b'{}'.format(hashable))
    return hash_object.hexdigest()

def accessed_today(last_accessed):
    """Return true if a shortenend url was accessed today
    """
    today = datetime.now().date()
    if last_accessed.date() == today:
        return True

def accessed_this_week(last_accessed):
    """Return true if a shortenend url was accessed this week
    """
    this_week = datetime.now().date().isocalendar()[1]
    print "this week is week", this_week
    if last_accessed.date().isocalendar()[1] == this_week:
        return True



if __name__ == '__main__':
    app.run(debug=True)

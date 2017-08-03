from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Surl(db.Model):
    __tablename__ = 'surls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    short_url = db.Column(db.String())
    last_accessed = db.Column(db.DateTime)
    day_count = db.Column(db.Integer)
    week_count = db.Column(db.Integer)
    all_time_count = db.Column(db.Integer)

    def __init__(self, url, short_url, day_count, week_count, all_time_count, last_accessed):
        self.url = url
        self.short_url = short_url
        self.last_accessed = last_accessed
        self.day_count = day_count
        self.week_count = week_count
        self.all_time_count = all_time_count

    def __repr__(self):
        return ('<id {} last_accessed {} url {} short_url'
                ' {} day_count {} week_count {} all_time_count {}>').format(
                self.id, 
                self.last_accessed, 
                self.url, 
                self.short_url,
                self.day_count,
                self.week_count,
                self.all_time_count
                )

def connect_to_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)
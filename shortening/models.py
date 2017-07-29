from app import db
from sqlalchemy.dialects.postgresql import JSON

class Surl(db.Model):
    __tablename__ = 'surls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    short_url = db.Column(db.String())
    day_count = db.Column(db.Integer)
    week_count = db.Column(db.Integer)
    all_time_count = db.Column(db.Integer)

    def __init__(self, url, short_url, day_count, week_count, all_time_count):
        self.url = url
        self.short_url = short_url
        self.day_count = day_count
        self.week_count = week_count
        self.all_time_count = all_time_count

    def __repr__(self):
        return '<id {}>'.format(self.id)
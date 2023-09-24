from database import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


class CorpusData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_age = db.Column(db.Integer)
    retirement_age = db.Column(db.Integer)
    corpus_goal = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    monthly_sip = db.Column(db.Float)
    closing_balance = db.Column(JSON)
    image_url = db.Column(db.String(255))

    def __init__(self, current_age, retirement_age, corpus_goal, interest_rate, monthly_sip, closing_balance, image_url):
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.corpus_goal = corpus_goal
        self.interest_rate = interest_rate
        self.monthly_sip = monthly_sip
        self.closing_balance = closing_balance
        self.image_url = image_url

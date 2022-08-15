from PassGen import db


class Account(db.Model):
    __tablename__ = "accounts"

    name = db.Column(db.Text)
    password = db.Column(db.Text)
    username = db.Column(db.Text)
    hint = db.Column(db.Text)
    last_updated = db.Column(db.DateTime)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)

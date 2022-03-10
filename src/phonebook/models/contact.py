from ..db import db


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=True)

    address = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=False)

    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)

    comment = db.Column(db.Text, nullable=True)

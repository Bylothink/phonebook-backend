from sqlalchemy import Index
from typing import Union

from ..db import db
from ..db.types import TSVector

__FULLTEXT__DEF__ = """to_tsvector('Italian', firstname || ' ' ||
                          COALESCE(lastname, '') || ' ' ||
                          COALESCE("address", '') || ' ' ||
                          COALESCE(comment, ''))"""


class Contact(db.Model):
    __tablename__ = 'contacts'

    @classmethod
    def Create(cls, firstname: str, phone: str,
                    lastname: Union[str, None] = None,
                    address: Union[str, None] = None,
                    lat: Union[float, None] = None,
                    lng: Union[float, None] = None,
                    comment: Union[str, None] = None):

        contact = cls(firstname=firstname, lastname=lastname, phone=phone,
                      address=address, lat=lat, lng=lng, comment=comment)

        db.session.add(contact)
        db.session.commit()

        return contact

    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=True)

    address = db.Column(db.String, nullable=True)
    phone = db.Column(db.String, nullable=False)

    lat = db.Column(db.Float, nullable=True)
    lng = db.Column(db.Float, nullable=True)

    comment = db.Column(db.Text, nullable=True)

    __fulltext__ = db.Column(TSVector, db.Computed(__FULLTEXT__DEF__, persisted=True))
    __table_args__ = (Index('contacts_fulltext_idx', __fulltext__, postgresql_using='gin'), )

    def update(self, firstname: Union[str, None] = None,
                     lastname: Union[str, None] = None,
                     address: Union[str, None] = None,
                     phone: Union[str, None] = None,
                     lat: Union[float, None] = None,
                     lng: Union[float, None] = None,
                     comment: Union[str, None] = None):

        if firstname is not None:
            self.firstname = firstname

        if lastname is not None:
            self.lastname = lastname

        if address is not None:
            self.address = address

        if phone is not None:
            self.phone = phone

        if lat is not None:
            self.lat = lat

        if lng is not None:
            self.lng = lng

        if comment is not None:
            self.comment = comment

        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

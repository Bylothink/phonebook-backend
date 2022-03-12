from sqlalchemy import Index
from typing import Union

from ..db import db
from ..db.types import TSVector

__FULLTEXT__DEF__ = """to_tsvector('english', firstname || ' ' ||
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
    __table_args__ = tuple(Index('contacts_fulltext', __fulltext__, postgresql_using='gin'))

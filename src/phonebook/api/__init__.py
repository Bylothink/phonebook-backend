from sqlalchemy import or_
from typing import List, Union

import strawberry
from strawberry.types import Info

from ..models import Contact
from .contact import ContactType

_TSQUERY_OPERATORS = ['&', '|', '!', '(', ')']


def to_tsquery(query: str) -> str:
    words = [word for word in query.split()]

    tsquery = words[0]
    for index in range(1, len(words)):
        prev_word = words[index - 1]
        this_word = words[index]

        if prev_word in _TSQUERY_OPERATORS or this_word in _TSQUERY_OPERATORS:
            tsquery += f" {this_word}"

        else:
            tsquery += f" & {this_word}"

    return tsquery


@strawberry.type
class Query:
    @strawberry.field
    def contact(self, info: Info, id: int) -> ContactType:
        return Contact.query.get(id)

    @strawberry.field
    def contacts(self, info: Info, query: Union[str, None] = None) -> List[ContactType]:
        if query:
            ts_query = to_tsquery(query)

            return Contact.query.filter(or_(
                # Contact.phone.match(query),  # SMELLS: «... match esatto...»?
                Contact.phone.ilike(f"%{query}%"),
                Contact.__fulltext__.match(ts_query, postgresql_regconfig='Italian')
            )).all()

        return Contact.query.all()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_contact(self, info: Info, firstname: str, phone: str,
                                         lastname: Union[str, None] = None,
                                         address: Union[str, None] = None,
                                         lat: Union[float, None] = None,
                                         lng: Union[float, None] = None,
                                         comment: Union[str, None] = None) -> ContactType:

        return Contact.Create(firstname, phone, lastname, address, lat, lng, comment)

    @strawberry.mutation
    def update_contact(self, info: Info, id: int,
                                         firstname: Union[str, None] = None,
                                         lastname: Union[str, None] = None,
                                         address: Union[str, None] = None,
                                         phone: Union[str, None] = None,
                                         lat: Union[float, None] = None,
                                         lng: Union[float, None] = None,
                                         comment: Union[str, None] = None) -> ContactType:

        contact: Contact = Contact.query.get(id)
        contact.update(firstname, lastname, phone, address, lat, lng, comment)

        return contact

    @strawberry.mutation
    def delete_contact(self, info: Info, id: int) -> bool:
        contact: Contact = Contact.query.get(id)
        contact.delete()

        return True


schema = strawberry.Schema(query=Query, mutation=Mutation)

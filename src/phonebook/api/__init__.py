from typing import List, Union

import strawberry
from strawberry.types import Info

from .. import logging
from ..models import Contact as ContactModel
from .contact import Contact as GraphQLContact

_logger = logging.getLogger(__name__)


@strawberry.type
class Query:
    @strawberry.field
    def contact(self, info: Info, id: int) -> GraphQLContact:
        _logger.info(f"Retrieving the contact with ID #{id}...")

    @strawberry.field
    def contacts(self, info: Info, query: Union[str, None] = None) -> List[GraphQLContact]:
        _logger.info("Retrieving all the contacts...")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_contact(self, info: Info, firstname: str, phone: str,
                                         lastname: Union[str, None] = None,
                                         address: Union[str, None] = None,
                                         lat: Union[float, None] = None,
                                         lng: Union[float, None] = None,
                                         comment: Union[str, None] = None) -> GraphQLContact:

        _logger.info("Creating a new contact...")
        contact = ContactModel.Create(firstname, phone, lastname, address, lat, lng, comment)

        return contact

    @strawberry.mutation
    def update_contact(self, info: Info, id: int,
                                         firstname: Union[str, None] = None,
                                         lastname: Union[str, None] = None,
                                         address: Union[str, None] = None,
                                         phone: Union[str, None] = None,
                                         lat: Union[float, None] = None,
                                         lng: Union[float, None] = None,
                                         comment: Union[str, None] = None) -> GraphQLContact:

        _logger.info(f"Updating the contact with ID #{id}...")

    @strawberry.mutation
    def delete_contact(self, info: Info, id: int) -> GraphQLContact:
        _logger.info(f"Deleting the contact with ID #{id}...")


schema = strawberry.Schema(query=Query, mutation=Mutation)

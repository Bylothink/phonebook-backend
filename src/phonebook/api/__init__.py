from typing import List

import strawberry
from strawberry.types import Info

from .. import logging
from .contacts import Contact

_logger = logging.getLogger(__name__)


@strawberry.type
class Query:
    @strawberry.field
    def contact(self, info: Info, id: int) -> Contact:
        _logger.info(f"Retrieving the contact with ID #{id}...")

    @strawberry.field
    def contacts(self, info: Info) -> List[Contact]:
        _logger.info("Retrieving all the contacts...")


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_contact(self, info: Info) -> Contact:
        _logger.info("Creating a new contact...")

    @strawberry.mutation
    def update_contact(self, info: Info, id: int) -> Contact:
        _logger.info(f"Updating the contact with ID #{id}...")

    @strawberry.mutation
    def delete_contact(self, info: Info, id: int) -> Contact:
        _logger.info(f"Deleting the contact with ID #{id}...")


schema = strawberry.Schema(query=Query, mutation=Mutation)

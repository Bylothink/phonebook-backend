from typing import Union

import strawberry


@strawberry.type
class ContactType:
    id: int

    firstname: str
    lastname: Union[str, None]

    address: Union[str, None]
    phone: str

    lat: Union[float, None]
    lng: Union[float, None]

    comment: Union[str, None]

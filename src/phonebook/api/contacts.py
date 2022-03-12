import strawberry


@strawberry.type
class Contact:
    id: int
    firstname: str
    lastname: str
    address: str
    phone: str
    lat: float
    lng: float
    comment: str

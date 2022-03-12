from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.types import TypeDecorator


class TSVector(TypeDecorator):
    impl = TSVECTOR

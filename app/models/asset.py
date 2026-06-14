from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Asset(Base):
    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    vendor = Column(
        String,
        nullable=False,
    )

    product = Column(
        String,
        nullable=False,
    )

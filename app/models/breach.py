from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base


class Breach(Base):
    __tablename__ = "breaches"

    name = Column(
        String,
        primary_key=True,
    )

    title = Column(String)
    domain = Column(String)

    breach_date = Column(
        Date,
        nullable=False,
    )

    added_date = Column(
        DateTime,
        nullable=False,
    )

    modified_date = Column(DateTime)

    pwn_count = Column(
        Integer,
        nullable=False,
    )

    description = Column(Text)
    logo_path = Column(String)

    data_classes = Column(
        JSONB,
        nullable=False,
    )

    is_verified = Column(
        Boolean,
        default=False,
    )

    is_sensitive = Column(
        Boolean,
        default=False,
    )

    is_spam_list = Column(
        Boolean,
        default=False,
    )

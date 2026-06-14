from datetime import date
from datetime import datetime

from pydantic import BaseModel


class BreachResponse(BaseModel):
    name: str
    title: str | None
    domain: str | None

    breach_date: date

    added_date: datetime

    modified_date: datetime | None

    pwn_count: int

    description: str | None

    logo_path: str | None

    data_classes: list[str]

    is_verified: bool

    is_sensitive: bool

    is_spam_list: bool

    model_config = {
        "from_attributes": True
    }

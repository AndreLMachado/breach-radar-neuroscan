from datetime import date
from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Session

from app.models import Breach


def upsert_breach(
    db: Session,
    breach_data: dict,
) -> bool:
    breach = (
        db.query(Breach)
        .filter(
            Breach.name == breach_data["Name"]
        )
        .first()
    )

    created = False

    if not breach:
        breach = Breach(
            name=breach_data["Name"],
        )

        db.add(breach)

        created = True

    breach.title = breach_data["Title"]
    breach.domain = breach_data["Domain"]

    breach.breach_date = datetime.strptime(
        breach_data["BreachDate"],
        "%Y-%m-%d",
    ).date()

    breach.added_date = datetime.strptime(
        breach_data["AddedDate"],
        "%Y-%m-%dT%H:%M:%SZ",
    )

    breach.modified_date = datetime.strptime(
        breach_data["ModifiedDate"],
        "%Y-%m-%dT%H:%M:%SZ",
    )

    breach.pwn_count = breach_data["PwnCount"]

    breach.description = breach_data["Description"]

    breach.logo_path = breach_data["LogoPath"]

    breach.data_classes = breach_data["DataClasses"]

    breach.is_verified = breach_data["IsVerified"]

    breach.is_sensitive = breach_data["IsSensitive"]

    breach.is_spam_list = breach_data["IsSpamList"]

    return created


def get_breach_by_name(
    db: Session,
    name: str,
) -> Breach | None:
    return (
        db.query(Breach)
        .filter(
            Breach.name == name
        )
        .first()
    )

def get_breaches(
    db: Session,
    page: int,
    page_size: int,
    domain: str | None = None,
    data_class: str | None = None,
    breach_date_from: date | None = None,
    breach_date_to: date | None = None,
    added_date_from: datetime | None = None,
    added_date_to: datetime | None = None,
    min_pwn_count: int | None = None,
    max_pwn_count: int | None = None,
    is_verified: bool | None = None,
    is_sensitive: bool | None = None,
    is_spam_list: bool | None = None,
) -> list[Breach]:
    offset = (page - 1) * page_size

    query = db.query(Breach)

    if domain:
        query = query.filter(
            Breach.domain.ilike(f"%{domain}%")
        )

    if data_class:
        query = query.filter(
            Breach.data_classes.cast(String).ilike(f"%{data_class}%")
        )

    if breach_date_from:
        query = query.filter(
            Breach.breach_date >= breach_date_from
        )

    if breach_date_to:
        query = query.filter(
            Breach.breach_date <= breach_date_to
        )

    if added_date_from:
        query = query.filter(
            Breach.added_date >= added_date_from
        )

    if added_date_to:
        query = query.filter(
            Breach.added_date <= added_date_to
        )

    if min_pwn_count is not None:
        query = query.filter(
            Breach.pwn_count >= min_pwn_count
        )

    if max_pwn_count is not None:
        query = query.filter(
            Breach.pwn_count <= max_pwn_count
        )

    if is_verified is not None:
        query = query.filter(
            Breach.is_verified == is_verified
        )

    if is_sensitive is not None:
        query = query.filter(
            Breach.is_sensitive == is_sensitive
        )

    if is_spam_list is not None:
        query = query.filter(
            Breach.is_spam_list == is_spam_list
        )

    return (
        query
        .offset(offset)
        .limit(page_size)
        .all()
    )

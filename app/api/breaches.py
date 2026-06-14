from datetime import date
from datetime import datetime

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import get_breach_by_name
from app.repositories import get_breaches
from app.schemas import BreachResponse

router = APIRouter(
    prefix="/breaches",
    tags=["breaches"],
)


@router.get(
    "",
    response_model=list[BreachResponse],
)
def get_breaches_endpoint(
    page: int = 1,
    page_size: int = 20,
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
    db: Session = Depends(get_db),
):
    return get_breaches(
        db=db,
        page=page,
        page_size=page_size,
        domain=domain,
        data_class=data_class,
        breach_date_from=breach_date_from,
        breach_date_to=breach_date_to,
        added_date_from=added_date_from,
        added_date_to=added_date_to,
        min_pwn_count=min_pwn_count,
        max_pwn_count=max_pwn_count,
        is_verified=is_verified,
        is_sensitive=is_sensitive,
        is_spam_list=is_spam_list,
    )


@router.get(
    "/{name}",
    response_model=BreachResponse,
)
def get_breach_detail_endpoint(
    name: str,
    db: Session = Depends(get_db),
):
    breach = get_breach_by_name(
        db=db,
        name=name,
    )

    if not breach:
        raise HTTPException(
            status_code=404,
            detail="Breach not found",
        )

    return breach

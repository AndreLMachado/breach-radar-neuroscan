import httpx

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import sync_breaches

router = APIRouter(
    tags=["sync"],
)


@router.post("/sync")
def sync_endpoint(
    db: Session = Depends(get_db),
):
    try:
        return sync_breaches(db=db)

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="HIBP feed unavailable",
        )

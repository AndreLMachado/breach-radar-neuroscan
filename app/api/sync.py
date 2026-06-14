from fastapi import APIRouter
from fastapi import Depends
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
    return sync_breaches(db=db)

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import (
    create_asset,
    delete_asset,
    get_assets,
)
from app.schemas import (
    AssetCreate,
    AssetResponse,
)

router = APIRouter(
    prefix="/assets",
    tags=["assets"],
)


@router.post(
    "",
    response_model=AssetResponse,
)
def create_asset_endpoint(
    asset: AssetCreate,
    db: Session = Depends(get_db),
):
    return create_asset(
        db=db,
        asset_data=asset,
    )


@router.get(
    "",
    response_model=list[AssetResponse],
)
def get_assets_endpoint(
    db: Session = Depends(get_db),
):
    return get_assets(db=db)


@router.delete("/{asset_id}")
def delete_asset_endpoint(
    asset_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_asset(
        db=db,
        asset_id=asset_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Asset not found",
        )

    return {
        "message": "Asset deleted"
    }

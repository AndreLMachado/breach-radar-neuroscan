from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud import create_asset
from app.crud import delete_asset
from app.crud import get_assets
from app.database import get_db
from app.schemas import AssetCreate
from app.schemas import AssetResponse

app = FastAPI(
    title="Breach Radar",
    description="API para sincronizar vulnerabilidades da CISA",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post(
    "/assets",
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

@app.get(
    "/assets",
    response_model=list[AssetResponse],
)
def get_assets_endpoint(
    db: Session = Depends(get_db),
):
    return get_assets(db=db)

@app.delete("/assets/{asset_id}")
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

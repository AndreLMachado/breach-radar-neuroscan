from sqlalchemy.orm import Session

from app.models import Asset
from app.schemas import AssetCreate


def create_asset(
    db: Session,
    asset_data: AssetCreate,
) -> Asset:
    asset = Asset(
        vendor=asset_data.vendor,
        product=asset_data.product,
    )

    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset


def get_assets(
    db: Session,
) -> list[Asset]:
    return db.query(Asset).all()


def delete_asset(
    db: Session,
    asset_id: int,
) -> bool:
    asset = db.query(Asset).filter(
        Asset.id == asset_id
    ).first()

    if not asset:
        return False

    db.delete(asset)
    db.commit()

    return True

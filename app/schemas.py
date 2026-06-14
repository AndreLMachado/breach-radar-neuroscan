from pydantic import BaseModel
from pydantic import ConfigDict


class AssetCreate(BaseModel):
    vendor: str
    product: str


class AssetResponse(BaseModel):
    id: int
    vendor: str
    product: str

    model_config = ConfigDict(
        from_attributes=True
    )

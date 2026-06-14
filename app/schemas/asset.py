from pydantic import BaseModel


class AssetCreate(BaseModel):
    vendor: str
    product: str


class AssetResponse(BaseModel):
    id: int
    vendor: str
    product: str

    model_config = {
        "from_attributes": True
    }

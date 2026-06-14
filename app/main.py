from fastapi import FastAPI

from app.api import assets_router
from app.api import breaches_router
from app.api import sync_router

app = FastAPI(
    title="Breach Radar",
    description="API para consultar breaches da HIBP",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(assets_router)
app.include_router(breaches_router)
app.include_router(sync_router)

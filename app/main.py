from fastapi import FastAPI

from app.api import assets_router

app = FastAPI(
    title="Breach Radar",
    description="API para sincronizar vulnerabilidades da CISA",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(assets_router)

from fastapi import FastAPI

app = FastAPI(
    title="Breach Radar",
    description="API para sincronizar vulnerabilidades da CISA",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }


def test_create_asset():
    response = client.post(
        "/assets",
        json={
            "vendor": "Microsoft",
            "product": "Windows Server",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["vendor"] == "Microsoft"
    assert data["product"] == "Windows Server"
    assert "id" in data

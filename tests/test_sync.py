import respx
import httpx

from fastapi.testclient import TestClient
from httpx import Response

from app.clients.hibp import HIBP_BREACHES_URL
from app.main import app

client = TestClient(app)


def test_sync_breaches_creates_records():
    mock_breaches = [
        {
            "Name": "TestBreach",
            "Title": "Test Breach",
            "Domain": "test.com",
            "BreachDate": "2024-01-01",
            "AddedDate": "2024-01-02T00:00:00Z",
            "ModifiedDate": "2024-01-03T00:00:00Z",
            "PwnCount": 1000,
            "Description": "Test description",
            "LogoPath": "https://example.com/logo.png",
            "DataClasses": ["Email addresses", "Passwords"],
            "IsVerified": True,
            "IsSensitive": False,
            "IsSpamList": False,
        }
    ]

    with respx.mock:
        respx.get(HIBP_BREACHES_URL).mock(
            return_value=Response(
                200,
                json=mock_breaches,
            )
        )

        response = client.post("/sync")

    assert response.status_code == 200
    assert response.json()["created"] >= 0
    assert response.json()["updated"] >= 0


def test_sync_breaches_twice_does_not_duplicate():
    mock_breaches = [
        {
            "Name": "TestBreachTwice",
            "Title": "Test Breach Twice",
            "Domain": "twice.com",
            "BreachDate": "2024-01-01",
            "AddedDate": "2024-01-02T00:00:00Z",
            "ModifiedDate": "2024-01-03T00:00:00Z",
            "PwnCount": 2000,
            "Description": "Test description",
            "LogoPath": "https://example.com/logo.png",
            "DataClasses": ["Email addresses", "Passwords"],
            "IsVerified": True,
            "IsSensitive": False,
            "IsSpamList": False,
        }
    ]

    with respx.mock:
        respx.get(HIBP_BREACHES_URL).mock(
            return_value=Response(
                200,
                json=mock_breaches,
            )
        )

        first_response = client.post("/sync")
        second_response = client.post("/sync")

    assert first_response.status_code == 200
    assert second_response.status_code == 200

    assert second_response.json()["created"] == 0
    assert second_response.json()["updated"] >= 1

def test_sync_feed_timeout_returns_503():
    with respx.mock:
        respx.get(HIBP_BREACHES_URL).mock(
            side_effect=httpx.TimeoutException("timeout")
        )

        response = client.post("/sync")

    assert response.status_code == 503
    assert response.json() == {
        "detail": "HIBP feed unavailable"
    }

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_breaches_returns_list():
    response = client.get(
        "/breaches",
        params={
            "page": 1,
            "page_size": 5,
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5


def test_get_breach_by_name_returns_breach():
    response = client.get("/breaches/000webhost")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "000webhost"
    assert data["domain"] == "000webhost.com"


def test_get_breach_by_name_not_found():
    response = client.get("/breaches/not-found-breach")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Breach not found"
    }

def test_get_breaches_filtered_by_domain():
    response = client.get(
        "/breaches",
        params={
            "domain": "000webhost",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    assert "000webhost" in data[0]["domain"]


def test_get_breaches_filtered_by_verified():
    response = client.get(
        "/breaches",
        params={
            "is_verified": True,
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["is_verified"] is True


def test_get_breaches_filtered_by_data_class():
    response = client.get(
        "/breaches",
        params={
            "data_class": "passwords",
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        data_classes = [
            item.lower()
            for item in breach["data_classes"]
        ]

        assert "passwords" in data_classes


def test_get_breaches_filtered_by_min_pwn_count():
    response = client.get(
        "/breaches",
        params={
            "min_pwn_count": 10000000,
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["pwn_count"] >= 10000000


def test_get_breaches_filtered_by_added_date_range():
    response = client.get(
        "/breaches",
        params={
            "added_date_from": "2020-01-01T00:00:00",
            "added_date_to": "2020-12-31T23:59:59",
            "page_size": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for breach in data:
        assert breach["added_date"].startswith("2020")
